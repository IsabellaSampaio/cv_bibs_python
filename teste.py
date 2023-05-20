'''
import cv2
import pytesseract
from PIL import Image
import string
import re
img2 = cv2.imread("placa.jpg")
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
(T,Thresh1) = cv2.threshold(img, 44, 54, cv2.THRESH_TRUNC)
(T,Thresh3) = cv2.threshold(Thresh1, 43, 44, cv2.THRESH_BINARY)
(T,Thresh2) = cv2.threshold(Thresh3, 0 ,255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
(T,Thresh4) = cv2.threshold(Thresh2, 30, 255, cv2.CALIB_CB_ADAPTIVE_THRESH)
cv2.imshow("Imagem 01", Thresh4)
cv2.waitKey(0)''' 

''' 
from random import *
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"
,"R","S","T","U","V","W","X","Y","Z"]
num = ["0", "1", "2", "3", "4","5", "6", "7", "8", "9"]
a = 0
while(a>=0):
    x = randint (0,25)
    y = randint (0,25)
    z = randint (0,25)
    a = randint (0, 9)
    b = randint (0, 9)
    c = randint (0, 9)
    d = randint (0, 9)
    res = letras[x]+letras[y]+letras[z]+"-"+num[a]+num[b]+num[c]+num[d]
    print(res)
    a+=1
    
'''
