import os
import argparse
import random

class split_train_val:
    def __init__(self):
        self.directorio_origen = r"..\Deteccion\data\custom\images"
        self.directorio_destino = r"..\Deteccion\data\custom"

        #parser = argparse.ArgumentParser()
        #parser.add_argument("--directorio_origen", type=str, default="data/custom/images", help="Directorio donde se encuentran todas las imagenes y las etiquetas")
        #parser.add_argument("--directorio_destino", type=str, default="data/custom", help="directorio donde se escribira train y test txt")
        #opt = parser.parse_args()


    def run(self):
        path = self.directorio_origen

        files = os.listdir(path)
        random.shuffle(files)
        train = files[:int(len(files)*0.9)]
        val = files[int(len(files)*0.9):]

        with open('{}/train.txt'.format(self.directorio_destino), 'w') as f:
            for item in train:
                f.write("{}/{} \n".format(path, item))

        with open('{}/valid.txt'.format(self.directorio_destino), 'w') as f:
            for item in val:
                f.write("{}/{} \n".format(path, item))