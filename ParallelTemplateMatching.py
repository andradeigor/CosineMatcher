import numpy as np
import concurrent.futures
import cv2
import math


class ParallelTemplateMaching():

    def __init__(self, imagePath, templatePath, cpus):
        image = cv2.imread(imagePath)
        template = cv2.imread(templatePath)
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = self.template.shape
        W, H = self.image.shape
        self.mediaT = np.mean(self.template)  # media de valores de T
        self.results = np.zeros((W-w+1, H-h+1))
        self.cpus = cpus
        self.pool = len(self.results) // self.cpus

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

    def template(self, beggin, end):
        for x in range(beggin, end):
            for y in range(len(self.results[0])):
                print(x, y)
                self.results[x][y] = self.R(x, y)

    def templateMatching(self):
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.cpus) as executor:
            Calculates = []

            # intervals = [(i * self.pool, (i+1) * self.pool if i !=
            # self.cpus-1 else len(self.results)) for i in range(self.cpus)]
            for i in range(self.cpus):
                start = i * self.pool
                end = (i+1) * self.pool if i != self.cpus - \
                    1 else len(self.results)
                Calculates.append(executor.submit(self.template, start, end))
            concurrent.futures.as_completed(Calculates)
            # for i in concurrent.futures.as_completed(Calculates):
            # print(i.result())

        return self.results
