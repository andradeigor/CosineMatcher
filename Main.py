from cv2 import COLOR_BGR2GRAY
from mss import mss
import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import pygame
import time

def jump(keyboard ):
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def FindCano(screen, cano):
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    local = cv2.matchTemplate(screen_gray, cano, cv2.TM_CCOEFF_NORMED)
    corte = 0.9
    local_cord = np.where(local >= corte)
    for i in zip(*local_cord[::-1]):
        cv2.rectangle(screen, i, (i[0] + 50, i[1] + 40), (0,0,255),5)
    return screen, local_cord[::-1]


def findBird(screen):# [103,203,248] = BGR
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    lower = np.array([20,100,20])
    upper = np.array([30,255,255])
    local = cv2.inRange(screen, lower, upper)
    local = np.where(local)
    local = local[::-1]#local é uma array 2d, sendo a primeira os conjuntos dos x, e a segunda os dos y.
    if len(local[0]) >0:
        cv2.rectangle(screen, (local[0][0]-10,local[1][0]-10), (local[0][0] + 24, local[1][0] + 24), (0,255,255),5)
    screen = cv2.cvtColor(screen,cv2.COLOR_HSV2BGR)
    return screen, local





def main():
    cano = cv2.imread("./templates/cano_top.jpg")
    cano = cv2.cvtColor(cano,COLOR_BGR2GRAY)
    keyboard = Controller()
    clock = pygame.time.Clock()
    while True:
        clock.tick(20)
        with mss() as sct:
            monitor = {"top": 120, "left": 10, "width": 280, "height": 480}
            screen = np.array(sct.grab(monitor))
            #screen = cv2.imread("./templates/teste.png")
            screen,canoLocation = FindCano(screen, cano)
            screen,birdLocation = findBird(screen)
            distance= 0
            try:
                lineCano = canoLocation[1][0]+143
                cv2.line(screen, (0,lineCano),(280,lineCano), (0,0,255),5)
            except:
                lineCano= 200
                cv2.line(screen, (0,lineCano),(280,lineCano), (0,0,255),5)
            try:
                lineBird = (birdLocation[0][0], birdLocation[1][0])
                cv2.line(screen, lineBird, (birdLocation[0][0], lineCano), (0,0,255), 5)
                if(len(birdLocation)):
                    distance = birdLocation[1][0] - lineCano
                else:
                    distance = -100
            except:
                pass
            if(distance != 0 and distance > -60):
                print(distance)
                jump(keyboard)
                time.sleep(0.3)
            cv2.imshow("Eye", screen)
            cv2.waitKey(1)

if __name__ == "__main__":
    main()


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