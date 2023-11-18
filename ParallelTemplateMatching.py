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
    # Faz o calculo da média dos valores da imagem
    mediaI = np.mean(I[x:x+xt, y:y+yt])

    for xLinha in range(xt):
        for yLinha in range(yt):
            # Diminui a média dos valores obtidos
            T_Linha = T[xLinha][yLinha] - mediaT
            I_Linha = I[x+xLinha][y+yLinha] - mediaI
            # Faz o produto entre os valores
            r_num += (T_Linha)*(I_Linha)
            # Calcula o quadrado para o demoninador
            r_dem_T += (T_Linha)**2
            r_dem_I += (I_Linha)**2
    # Faz o calculo do denominador
    r_dem = (math.sqrt((r_dem_T*r_dem_I)))
    # Se o denominador for zero, retorna zero para não ter divisão por 0
    if (r_dem == 0):
        return 0
    r = r_num/r_dem
    return r


def template(I, T, beggin, end, mediaT):
    # Pega as dimensões das imagens
    w, h = T.shape
    W, H = I.shape
    # Cria uma nova matriz de resultados por conta de ser em um processo separado
    results = np.zeros((W-w+1, H-h+1))
    for x in range(beggin, end):
        for y in range(len(results[0])):
            # Faz o calculo do cosseno para cada uma das coordenadas que esse processo é responsável
            results[x][y] = R(x, y, I, T, mediaT)
    return results


class ParallelTemplateMaching():

    def __init__(self, imagePath, templatePath, cpus=cpu_count()):
        # Leitura das imagens
        self.imageColors = cv2.imread(imagePath)
        template = cv2.imread(templatePath)
        # Transformação da escala de cor para cinza, isso diminui em 3x o tamanho a imagem
        self.image = cv2.cvtColor(self.imageColors, cv2.COLOR_BGR2GRAY)
        self.template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        self.mediaT = np.mean(self.template)  # media de valores de T
        self.cpus = cpus
        # Tamanho das imagens
        self.w, self.h = self.template.shape
        W, H = self.image.shape
        # A matriz de resultados e a quantidade de linhas que cada processo vai calcular
        self.results = np.zeros((W-self.w+1, H-self.h+1))
        self.pool = len(self.results) // self.cpus

    # Abre uma janela com a imagem
    def print(self):
        cv2.imshow("Print", self.imageColors)
        cv2.waitKey(0)
    # Desenha os quadrados, uma vez que o calculo das coordenadas foi feito

    def drawRectangles(self, cordinates):
        for i in zip(*cordinates[::-1]):
            cv2.rectangle(
                self.imageColors, i, (i[0] + self.h, i[1] + self.w), (0, 0, 255), 5)

    def templateMatching(self):

        with ProcessPoolExecutor(max_workers=self.cpus) as executor:
            Calculates = []
            # Faz o calculo dos intervalores, calculando quantas linhas cada processo vai calcular
            cordinates = [(i * self.pool, (i+1) * self.pool if i !=
                           self.cpus-1 else len(self.results)) for i in range(self.cpus)]

            for start, end in cordinates:
                # Cria um processo com as linhas iniciais e finais
                Calculates.append(executor.submit(
                    template, self.image, self.template, start, end, self.mediaT))

            for i, future in enumerate(Calculates):
                # pega o resultado do calculo
                result = future.result()
                start, end = cordinates[i]
                # transfere o resultado para a matriz de resultados
                self.results[start:end, ::] = result[start:end, ::]

        return self.results
