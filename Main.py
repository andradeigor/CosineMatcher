from mss import mss
import cv2
import numpy as np
#while True:
#    with mss() as sct:
#        monitor = {"top": 80, "left": 10, "width": 280, "height": 480}
#        screen = np.array(sct.grab(monitor))
screen = cv2.imread("./templates/cano_top.jpg")
cv2.imshow("Eye", screen)
cv2.waitKey(0)