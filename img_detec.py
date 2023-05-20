import numpy as np
import cv2
import mahotas
import pytesseract

#Função para facilitar a escrita nas imagem
def escreve(img, texto, cor=(255,0,0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0,
    cv2.LINE_AA)

def identificar_numeros(img):
    # Converte a imagem para tons de cinza
    img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Binariza a imagem com thresholding adaptativo
    img_bin = cv2.adaptiveThreshold(img_cinza, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, blockSize=15, C=8)
    
    # Encontra os contornos dos dígitos
    objetos_digitos = []
    for c in cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
        # Calcula o retângulo que envolve o contorno
        (x, y, w, h) = cv2.boundingRect(c)
        # Se o retângulo for muito pequeno, provavelmente não é um dígito
        if w > 30 and h > 30:
            # Recorta a imagem correspondente ao retângulo
            roi = img_cinza[y:y+h, x:x+w]
            objetos_digitos.append(roi)
    
    # Reconhece os caracteres em cada imagem de dígito utilizando o Tesseract OCR
    numeros = []
    for obj in objetos_digitos:
        texto = pytesseract.image_to_string(obj, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        
        if texto.strip():
            numeros.append(int(texto.strip()))
        else:
            numeros.append(None)
        
    # Desenha retângulos ao redor dos dígitos encontrados
    img_com_retangulos = img.copy()
    for c in cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
        (x, y, w, h) = cv2.boundingRect(c)
        if w > 15 and h > 15:
            cv2.rectangle(img_com_retangulos, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(numeros)
    return numeros, img_com_retangulos
    
imgColorida = cv2.imread('dados.jpg') #Carregamento da imagem
#Se necessário o redimensionamento da imagem pode vir aqui.
#Passo 1: Conversão para tons de cinza
img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)
#Passo 2: Blur/Suavização da imagem
suave = cv2.blur(img, (7, 7))
#Passo 3: Binarização resultando em pixels brancos e pretos
T = mahotas.thresholding.otsu(suave)
bin = suave.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin)
#Passo 4: Detecção de bordas com Canny

bordas = cv2.Canny(bin, 70, 150)
#Passo 5: Identificação e contagem dos contornos da imagem
#cv2.RETR_EXTERNAL = conta apenas os contornos externos
(objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
#A variável lx (lixo) recebe dados que não

escreve(img, "Imagem em tons de cinza", 0)
escreve(suave, "Suavizacao com Blur", 0)
escreve(bin, "Binarizacao com Metodo Otsu", 255)
escreve(bordas, "Detector de bordas Canny", 255)
temp = np.vstack([
np.hstack([img, suave]),
np.hstack([bin, bordas])
])
imgC2 = imgColorida.copy()

try:
    cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
    
except:
    pass
escreve(imgC2, str(len(objetos))+" objetos encontrados!")
cv2.imwrite("Resultado.jpg", imgC2)

##proximo passo, identificar os números nos dados

numeros, img_com_retangulos = identificar_numeros(imgC2)
cv2.imwrite("Resultado2.jpg", img_com_retangulos)
