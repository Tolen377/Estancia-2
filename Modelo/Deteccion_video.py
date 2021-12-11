from __future__ import division
#from models import *
#from utils.utils import *
#from utils.datasets import *
import os
import sys
import argparse
import cv2
from PIL import Image
import torch
from torch.autograd import Variable

from Deteccion.models import *
from Deteccion.utils.utils import *
from Deteccion.utils.datasets import *


class deteccion_video:
    def __init__(self,directorio_video,directorio_checkpoint):

        # Atributos de la clase deteccion video para poder usar la clase como objeto
        self.webcam = 0
        self.directorio_video = directorio_video
        self.model_def = r"..\Deteccion\config\yolov3-custom.cfg"
        self.checkpoint_model = directorio_checkpoint
        self.class_path = r"..\Deteccion\data\custom\classes.names"
        self.weights_path = directorio_checkpoint
        self.conf_thres = 0.85
        self.img_size = 416
        self.nms_thres = 0.4
        self.identificaciones = 0



    def getIdentificaciones(self):
        return self.identificaciones


    def Convertir_RGB(self,img):
        # Convertir Blue, green, red a Red, green, blue
        b = img[:, :, 0].copy()
        g = img[:, :, 1].copy()
        r = img[:, :, 2].copy()
        img[:, :, 0] = r
        img[:, :, 1] = g
        img[:, :, 2] = b
        return img


    def Convertir_BGR(self,img):
        # Convertir red, blue, green a Blue, green, red
        r = img[:, :, 0].copy()
        g = img[:, :, 1].copy()
        b = img[:, :, 2].copy()
        img[:, :, 0] = b
        img[:, :, 1] = g
        img[:, :, 2] = r
        return img



    def main(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print("cuda" if torch.cuda.is_available() else "cpu")
        model = Darknet(self.model_def, img_size=self.img_size).to(device)
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


        if self.weights_path.endswith(".weights"):
            model.load_darknet_weights(self.weights_path)
        else:
            model.load_state_dict(torch.load(self.weights_path))

        model.eval()
        classes = load_classes(self.class_path)
        Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor
        if self.webcam==1:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter(desktop+'\output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1280,960))
        else:
            cap = cv2.VideoCapture(self.directorio_video)
            # frame_width = int(cap.get(3))
            # frame_height = int(cap.get(4))
            out = cv2.VideoWriter(desktop+'\output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (1280,960))
        colors = np.random.randint(0, 255, size=(len(classes), 3), dtype="uint8")
        a=[]
        while cap:
            ret, frame = cap.read()
            if ret is False:
                break
            frame = cv2.resize(frame, (1280, 960), interpolation=cv2.INTER_CUBIC)
            #LA imagen viene en Blue, Green, Red y la convertimos a RGB que es la entrada que requiere el modelo
            RGBimg=self.Convertir_RGB(frame)
            imgTensor = transforms.ToTensor()(RGBimg)
            imgTensor, _ = pad_to_square(imgTensor, 0)
            imgTensor = resize(imgTensor, 416)
            imgTensor = imgTensor.unsqueeze(0)
            imgTensor = Variable(imgTensor.type(Tensor))


            with torch.no_grad():
                detections = model(imgTensor)
                detections = non_max_suppression(detections, self.conf_thres, self.nms_thres)


            for detection in detections:
                if detection is not None:
                    detection = rescale_boxes(detection, self.img_size, RGBimg.shape[:2])
                    for x1, y1, x2, y2, conf, cls_conf, cls_pred in detection:
                        box_w = x2 - x1
                        box_h = y2 - y1
                        color = [int(c) for c in colors[int(cls_pred)]]
                        print("Se detectó {} en X1: {}, Y1: {}, X2: {}, Y2: {}".format(classes[int(cls_pred)], x1, y1, x2, y2))
                        frame = cv2.rectangle(frame, (int(x1), int(y1 + box_h)), (int (x2), int (y1)), color, 5)
                        cv2.putText(frame, classes[int(cls_pred)], (int(x1), int( y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 5)# Nombre de la clase detectada
                        cv2.putText(frame, str("%.2f" % float(conf)), (int(x2), int (y2 - box_h)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,color, 5) # Certeza de prediccion de la clase
                        self.identificaciones += 1
            #
            #Convertimos de vuelta a BGR para que cv2 pueda desplegarlo en los colores correctos
            #----------

            if self.webcam==1:
                cv2.imshow('frame', self.Convertir_BGR(RGBimg))
                out.write(RGBimg)
            else:
                out.write(self.Convertir_BGR(RGBimg))
                cv2.imshow('frame', RGBimg)
            #cv2.waitKey(0)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        out.release()
        cap.release()
        cv2.destroyAllWindows()