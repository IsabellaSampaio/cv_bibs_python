import cv2
imagem = cv2.imread('ponte.jpg')
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (255,0,0)
        break
cv2.imwrite("imagem_modificada.jpg", imagem)