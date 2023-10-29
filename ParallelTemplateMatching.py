from multiprocessing import cpu_count, Process, Manager
import numpy as np
import cv2
import math
import time


class Calculate(Process):
    def __init__(self, image, template, beggin, end, mediaT, results):
        super(Calculate, self).__init__()
        self.image = image
        self.template = template
        self.beggin = beggin
        self.end = end
        self.mediaT = mediaT
        self.results = results

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
        for x in range(self.beggin, self.end):
            for y in range(len(self.results[0])):
                self.results[x][y] = self.R(x, y)


class ParallelTemplateMaching():

    def __init__(self, imagePath, templatePath, cpus=cpu_count()):
        image = cv2.imread(imagePath)
        template = cv2.imread(templatePath)
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        self.cpus = cpus
        w, h = self.template.shape
        W, H = self.image.shape
        self.mediaT = np.mean(self.template)  # media de valores de T
        self.results = np.zeros((W-w+1, H-h+1))
        self.pool = len(self.results) // self.cpus

    def print(self):
        cv2.imshow("Print", self.image)
        cv2.waitKey(0)

    def run(self):
        Calculates = []

        with Manager() as manager:
            matrix = manager.list(self.results)
            for i in range(self.cpus):
                start = i * self.pool
                end = (i+1) * self.pool if i != self.cpus else len(self.results)
                c = Calculate(self.image, self.template, start,
                              end, self.mediaT, matrix)
                Calculates.append(c)
                c.start()

            for i in range(self.cpus):
                Calculates[i].join()
            for row in matrix:
                print(row)
        return self.results
