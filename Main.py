from cv2 import COLOR_BGR2GRAY
from mss import mss
import cv2
import numpy as np
from scipy import spatial
while True:
   with mss() as sct:
        monitor = {"top": 180, "left": 10, "width": 280, "height": 480}
        screen = np.array(sct.grab(monitor))
        cano = cv2.imread("./templates/cano_top.jpg")
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY).flatten()
        cano = cv2.cvtColor(cano,COLOR_BGR2GRAY).flatten()
        size = len(cano)
        for i in range(0,len(screen_gray)-len(cano),20):
            cos = -1*(spatial.distance.cosine(cano,screen_gray[i:i+size])-1)
            print(cos)
            if(cos > 0.94):
                screen = cv2.rectangle(screen, (i//287,i%287), ((i//287) + 50,(i%287) + 30), (0,0,255),5)
                break
        cv2.imshow("Eye", screen)
        cv2.waitKey(1)





"""
def cosine(a,b):
    interProduct = 0
    for i in range(len(a)):
        interProduct+= int(a[i]) * int(b[i])
    normA = np.linalg.norm(a)
    normB = np.linalg.norm(b)
    return interProduct/(normA*normB)
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
teste = cv2.cvtColor(teste, cv2.COLOR_BGR2GRAY)

screen = screen.flatten()
teste_flatten = teste.flatten()
size = len(screen)

for i in range(0,len(teste_flatten)-len(screen)):
    cos = spatial.distance.cosine(screen,teste_flatten[i:i+size])
    if(cos > 0.94):
        teste = cv2.rectangle(teste, (i//287,i%287), ((i//287) + 50,(i%287) + 30), (0,0,255),5)
        cv2.imshow("Eye", teste)
        cv2.waitKey(0)

"""

#for i in screen:
#    for k in i:
#        print(k)
#cv2.imshow("Eye", screen)
#cv2.waitKey(0)