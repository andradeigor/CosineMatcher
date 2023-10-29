from cv2 import CV_8U
import numpy as np
import math
import cv2
import time


def TLinha(x, y, T, mediaT):
    return T[x][y] - mediaT


def ILinha(x, y, I, mediaI):
    return I[x][y] - mediaI


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


def template_matching(I, T):
    w, h = T.shape
    W, H = I.shape
    mediaT = np.mean(T)  # media de valores de T
    results = np.zeros((W-w+1, H-h+1))
    total = (W-w+1) * (H-h+1)
    done = 0
    for x in range(len(results)):
        for y in range(len(results[0])):
            results[x][y] = R(x, y, I, T, mediaT)
            done += 1
            print(f"fiz:{done} de {total}")
    return results


def main():
    inicio = time.time()
    T = cv2.imread("./templates/btgtemplate.jpg")
    T_gray = cv2.cvtColor(T, cv2.COLOR_BGR2GRAY)
    I = cv2.imread("./templates/btgimage.jpg")
    I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    y, x, _ = T.shape
    result_1 = template_matching(I_gray, T_gray)
    local_cord = np.where(result_1 >= 0.8)
    for i in zip(*local_cord[::-1]):
        cv2.rectangle(I, i, (i[0] + x, i[1] + y), (0, 0, 255), 5)
    fim = time.time()
    print(inicio-fim)
    cv2.imshow("Eye", I)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
