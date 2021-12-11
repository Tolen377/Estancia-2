from __future__ import division

from Deteccion.models import *
from Deteccion.utils.logger import *
from Deteccion.utils.utils import *
from Deteccion.utils.datasets import *
from Deteccion.utils.parse_config import *
from Deteccion.test import evaluate

from terminaltables import AsciiTable

import os
import sys
import time
import datetime
import argparse

import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from torch.autograd import Variable
import torch.optim as optim



class Train:
    def __init__(self):
        self.model_def = r"..\Deteccion\config\yolov3-custom.cfg"
        self.data_config = r"..\Deteccion\config\custom.data"
        self.pretrained_weights = r"..\Deteccion\weights\darknet53.conv.74"
        self.batch_size = 2
        self.epochs = 100
        self.gradient_accumulations = 2
        self.n_cpu = 8
        self.img_size = 416
        self.checkpoint_interval = 1
        self.evaluation_interval = 1
        self.compute_map = False
        self.multiscale_training = True
        #-------------------------------------->


    def run(self):
        logger = Logger(r"..\Deteccion\logs")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        os.makedirs(r"..\Deteccion\output", exist_ok=True)
        os.makedirs(r"..\Deteccion\checkpoints", exist_ok=True)

        # Get data configuration
        data_config = parse_data_config(self.data_config)
        train_path = data_config["train"]
        valid_path = data_config["valid"]
        class_names = load_classes(data_config["names"])

        # Initiate model
        model = Darknet(self.model_def).to(device)
        model.apply(weights_init_normal)

        # If specified we start from checkpoint
        if self.pretrained_weights:
            if self.pretrained_weights.endswith(".pth"):
                model.load_state_dict(torch.load(self.pretrained_weights))
            else:
                model.load_darknet_weights(self.pretrained_weights)

        # Get dataloader
        dataset = ListDataset(train_path, augment=True, multiscale=self.multiscale_training)
        dataloader = torch.utils.data.DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.n_cpu,
            pin_memory=True,
            collate_fn=dataset.collate_fn,
        )

        optimizer = torch.optim.Adam(model.parameters())

        metrics = [
            "grid_size",
            "loss",
            "x",
            "y",
            "w",
            "h",
            "conf",
            "cls",
            "cls_acc",
            "recall50",
            "recall75",
            "precision",
            "conf_obj",
            "conf_noobj",
        ]

        for epoch in range(self.epochs):
            model.train()
            start_time = time.time()
            for batch_i, (_, imgs, targets) in enumerate(dataloader):
                batches_done = len(dataloader) * epoch + batch_i

                imgs = Variable(imgs.to(device))
                targets = Variable(targets.to(device), requires_grad=False)

                loss, outputs = model(imgs, targets)
                loss.backward()

                if batches_done % self.gradient_accumulations:
                    # Accumulates gradient before each step
                    optimizer.step()
                    optimizer.zero_grad()

                # ----------------
                #   Log progress
                # ----------------

                log_str = "\n---- [Epoch %d/%d, Batch %d/%d] ----\n" % (epoch, self.epochs, batch_i, len(dataloader))

                metric_table = [["Metrics", *[f"YOLO Layer {i}" for i in range(len(model.yolo_layers))]]]

                # Log metrics at each YOLO layer
                for i, metric in enumerate(metrics):
                    formats = {m: "%.6f" for m in metrics}
                    formats["grid_size"] = "%2d"
                    formats["cls_acc"] = "%.2f%%"
                    row_metrics = [formats[metric] % yolo.metrics.get(metric, 0) for yolo in model.yolo_layers]
                    metric_table += [[metric, *row_metrics]]

                    # Tensorboard logging
                    tensorboard_log = []
                    for j, yolo in enumerate(model.yolo_layers):
                        for name, metric in yolo.metrics.items():
                            if name != "grid_size":
                                tensorboard_log += [(f"{name}_{j+1}", metric)]
                    tensorboard_log += [("loss", loss.item())]
                    logger.list_of_scalars_summary(tensorboard_log, batches_done)

                log_str += AsciiTable(metric_table).table
                log_str += f"\nTotal loss {loss.item()}"

                # Determine approximate time left for epoch
                epoch_batches_left = len(dataloader) - (batch_i + 1)
                time_left = datetime.timedelta(seconds=epoch_batches_left * (time.time() - start_time) / (batch_i + 1))
                log_str += f"\n---- ETA {time_left}"

                print(log_str)

                model.seen += imgs.size(0)

            if epoch % self.evaluation_interval == 1:
                print("\n---- Evaluating Model ----")
                # Evaluate the model on the validation set
                precision, recall, AP, f1, ap_class = evaluate(
                    model,
                    path=valid_path,
                    iou_thres=0.5,
                    conf_thres=0.5,
                    nms_thres=0.5,
                    img_size=self.img_size,
                    batch_size=8,
                )
                evaluation_metrics = [
                    ("val_precision", precision.mean()),
                    ("val_recall", recall.mean()),
                    ("val_mAP", AP.mean()),
                    ("val_f1", f1.mean()),
                ]
                logger.list_of_scalars_summary(evaluation_metrics, epoch)

                # Print class APs and mAP
                ap_table = [["Index", "Class name", "AP"]]
                for i, c in enumerate(ap_class):
                    ap_table += [[c, class_names[c], "%.5f" % AP[i]]]
                print(AsciiTable(ap_table).table)
                print(f"---- mAP {AP.mean()}")

            if epoch % self.checkpoint_interval == 0:
                torch.save(model.state_dict(), r"..\Deteccion\checkpoints\yolov3_ckpt_%d.pth" % epoch)
