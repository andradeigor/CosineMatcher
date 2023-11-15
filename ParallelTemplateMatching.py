import numpy as np
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
import cv2
import math


def R(x, y, I, T, mediaT):
    xt, yt = T.shape
    r_num = 0
    r_dem_T = 0
    r_dem_I = 0
    mediaI = np.mean(I[x:x+xt, y:y+yt])

    for xLinha in range(xt):
        for yLinha in range(yt):
            T_Linha = T[xLinha][yLinha] - mediaT
            I_Linha = I[x+xLinha][y+yLinha] - mediaI
            r_num += (T_Linha)*(I_Linha)
            r_dem_T += (T_Linha)**2
            r_dem_I += (I_Linha)**2

    r_dem = (math.sqrt((r_dem_T*r_dem_I)))
    if (r_dem == 0):
        return 0
    r = r_num/r_dem
    return r


def template(I, T, beggin, end):
    w, h = T.shape
    W, H = I.shape
    mediaT = np.mean(T)  # media de valores de T
    results = np.zeros((W-w+1, H-h+1))
    for x in range(beggin, end):
        for y in range(len(results[0])):
            results[x][y] = R(x, y, I, T, mediaT)
    return results


class ParallelTemplateMaching():

    def __init__(self, imagePath, templatePath, cpus=cpu_count()):
        self.imageColors = cv2.imread(imagePath)
        template = cv2.imread(templatePath)
        self.image = cv2.cvtColor(self.imageColors, cv2.COLOR_BGR2GRAY)
        self.template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        self.mediaT = np.mean(self.template)  # media de valores de T
        self.cpus = cpus
        self.w, self.h = self.template.shape
        W, H = self.image.shape
        self.results = np.zeros((W-self.w+1, H-self.h+1))
        self.pool = len(self.results) // self.cpus

    def print(self):
        cv2.imshow("Print", self.imageColors)
        cv2.waitKey(0)

    def drawRectangles(self, cordinates):
        for i in zip(*cordinates[::-1]):
            cv2.rectangle(
                self.imageColors, i, (i[0] + self.h, i[1] + self.w), (0, 0, 255), 5)

    def templateMatching(self):

        with ProcessPoolExecutor(max_workers=self.cpus) as executor:
            Calculates = []
            cordinates = [(i * self.pool, (i+1) * self.pool if i !=
                           self.cpus-1 else len(self.results)) for i in range(self.cpus)]
            for start, end in cordinates:
                Calculates.append(executor.submit(
                    template, self.image, self.template, start, end))

            for i, future in enumerate(Calculates):
                result = future.result()
                start, end = cordinates[i]
                self.results[start:end, ::] = result[start:end, ::]
        self.drawRectangles(np.where(self.results >= 0.8))
        self.print()
        return self.results
