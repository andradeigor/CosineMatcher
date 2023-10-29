from multiprocessing import cpu_count
import numpy as np
import cv2
import math
import time


class TemplateMaching():

    def __init__(self, imagePath, templatePath, cpus=cpu_count()):
        image = cv2.imread(imagePath)
        template = cv2.imread(templatePath)
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        self.linhas, self.colunas, _ = image.shape
        self.cpus = cpus

    def print(self):
        cv2.imshow("Print", self.image)
        cv2.waitKey(0)

    def R(self, x, y):
        xt, yt = self.template.shape
        r_num = 0
        r_dem_T = 0
        r_dem_I = 0
        mediaI = np.mean(self.image[x:x+xt, y:y+yt])

        for xLinha in range(xt):
            for yLinha in range(yt):
                templateLinha = self.template[xLinha][yLinha] - self.mediaT
                imageLinha = self.image[x+xLinha][y+yLinha] - mediaI
                r_num += (templateLinha)*(imageLinha)
                r_dem_T += (templateLinha)**2
                r_dem_I += (imageLinha)**2

        r_dem = (math.sqrt((r_dem_T*r_dem_I)))
        if (r_dem == 0):
            return 0
        r = r_num/r_dem
        return r

    def run(self):
        w, h = self.template.shape
        W, H = self.image.shape
        self.mediaT = np.mean(self.template)  # media de valores de T
        self.results = np.zeros((W-w+1, H-h+1))
        total = (W-w+1) * (H-h+1)
        done = 0
        for x in range(len(self.results)):
            for y in range(len(self.results[0])):
                self.results[x][y] = self.R(x, y,)
                done += 1
                print(f"fiz:{done} de {total}")
        return self.results
