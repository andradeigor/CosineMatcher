import numpy as np
import math

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
    r = r_num/(math.sqrt((r_dem_T*r_dem_I))) 
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
    #I = np.array([[1.0,1.0,2.0,3.0],[2.0,3.0,4.0,5.0],
    #[3.0,4.0,5.0,6.0],[3.0,4.0,5.0,6.0]])
    #T = np.array([[4.0,5.0], [5.0, 6.1]])
    I = np.random.randint(100,size=(4,4))
    T = I[0:2,2:4]
    result = template_matching(I,T)
    for i in I:
        print(i)
    print("==================")
    for i in T:
        print(i)
    print("==================")
    for i in result:
        print(i)
if __name__ == "__main__":
    main()