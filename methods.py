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
            T_Linha =TLinha(xLinha,yLinha, T, mediaT)
            I_Linha = ILinha(x+xLinha,y+yLinha,I,mediaI) 
            r_num+= T_Linha*I_Linha 
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
    print(results.shape)
    for x in range(len(results)):
        for y in range(len(results[0])):
            results[x][y] = R(x,y,I,T,mediaT)
            print(x*len(results[0])+y)
    return results


def main():
    template = cv2.imread("./templates/cano_top.png")
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    Image = cv2.imread("./templates/teste.png")
    Image_gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    x,y,z = template.shape
    I = np.random.randint(100,size=(5,6))
    T = I[1:3,1:3]
    #result = template_matching(Image_gray,template_gray)
    result = cv2.matchTemplate(Image_gray, template_gray,cv2.TM_CCOEFF_NORMED)
    Image = cv2.rectangle(Image,(181,37), (181+y,37+x),(0,0,255), 5)
    cv2.imshow("Eye", Image)
    cv2.waitKey(0)
    print(np.unravel_index(np.argmax(result, axis=None), result.shape))
if __name__ == "__main__":
    main()