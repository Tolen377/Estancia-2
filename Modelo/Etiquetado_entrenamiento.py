from Modelo.split_train_val import split_train_val
from Modelo.train import Train
import labelImg.labelImg
import os
import glob
from os import remove
from os import path


class Etiquetado_entrenamiento:
    def __init__(self):
        self.etiquetado = split_train_val()
        self.train = Train()
        self.rutaFinal = ""




    def getRutaFinal(self):
        return self.rutaFinal


    def Etiquetado(self):
        labelImg.labelImg.main()
        self.etiquetado.run()


    def Entrenamiento(self):
        nombreOriginal = "..\Deteccion\checkpoints\yolov3_ckpt_99.pth"
        z = 0


        #Comienza el entrenamiento
        self.train.run()

        #Borrar los checkpoint sobrantes
        for i in range(0, 99):
            x = str(i)
            remove(r"..\Deteccion\checkpoints\yolov3_ckpt_" + x + ".pth")


        #Renombra el checkpoint por uno secuencial
        while os.path.exists("..\Deteccion\checkpoints\yolov3_ckpt_99_%s.pth" % z):
            z += 1
        os.rename(nombreOriginal,"..\Deteccion\checkpoints\yolov3_ckpt_99_%s.pth" % z)
        self.rutaFinal = os.path.abspath("..\Deteccion\checkpoints\yolov3_ckpt_99_%s.pth" % z)


        # Borrar el archivo de train.txt
        if path.exists(r"..\Deteccion\data\custom\train.txt"):
            remove(r"..\Deteccion\data\custom\train.txt")
        else:
            print("no existe")

        # Borrar el archivo de valid.txt
        if path.exists(r"..\Deteccion\data\custom\valid.txt"):
            remove(r"..\Deteccion\data\custom\valid.txt")
        else:
            print("no existe")

        # Busca patrones de archivos txt para borrar los labels
        labels = glob.glob(r'..\Deteccion\data\custom\labels\*.txt')
        # Los borra
        for label in labels:
            try:
                os.remove(label)
            except OSError as e:
                print(f"Error:{e.strerror}")

