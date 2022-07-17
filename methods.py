from cv2 import CV_8U
import numpy as np
import math
import cv2
def TLinha(x,y,T, mediaT):
    return T[x][y] - mediaT

def ILinha(x,y,I,mediaI):
    return I[x][y] - mediaI 


def R(x,y,I,T,mediaT):
    xt,yt = T.shape
    r_num = 0
    r_dem_T = 0
    r_dem_I = 0
    mediaI = np.mean(I[x:x+xt, y:y+yt])

    for xLinha in range(xt):
        for yLinha in range(yt):
            T_Linha = T[xLinha][yLinha] - mediaT
            I_Linha = I[x+xLinha][y+yLinha] - mediaI 
            r_num+= (T_Linha)*(I_Linha) 
            r_dem_T+= (T_Linha)**2
            r_dem_I += (I_Linha)**2

    r_dem = (math.sqrt((r_dem_T*r_dem_I)))
    if(r_dem ==0):
        return 0
    r = r_num/r_dem
    return r

def template_matching(I,T):
    w,h = T.shape
    W,H = I.shape
    mediaT = np.mean(T)#media de valores de T
    results = np.zeros((W-w+1,H-h+1))
    for x in range(len(results)):
        for y in range(len(results[0])):
            results[x][y] = R(x,y,I,T,mediaT)
    return results


def main():
    template = cv2.imread("./templates/cano_top.png")
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    Image = cv2.imread("./templates/teste.png")
    Image_gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

    x,y,_ = template.shape
    result_1 = template_matching(Image_gray,template_gray)
    
    result_1 = np.unravel_index(np.argmax(result_1, axis=None), result_1.shape)
    Image = cv2.rectangle(Image, result_1, (result_1[1] + y, result_1[0] + x), (0,0,255),5)
    cv2.imshow("Eye", Image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()







    x,y,z = template.shape
    #for i in range(100):
    #I = np.random.randint(255,size=(5,6))
    #I = np.uint8(I)
    #T = I[1:3,1:3]
    #result_2 = cv2.matchTemplate(I, T,cv2.TM_CCOEFF_NORMED)
    result_1 = np.unravel_index(np.argmax(result_1, axis=None), result_1.shape)
    #result_2 =  np.unravel_index(np.argmax(result_2, axis=None), result_2.shape)
    