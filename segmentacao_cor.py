import cv2
import numpy as np
from PIL import Image
from glob import glob

# Redimensionar foto
img = Image.open("faixa-horizontal-opencv/fotos/faixaFoto5.jpg")
img = img.resize((round(400), round(300)), Image.BILINEAR)
img.save( 'faixa-horizontal-opencv/fotos/imagemRedimensionada.jpg', 'JPEG' )

image = cv2.imread("faixa-horizontal-opencv/fotos/imagemRedimensionada.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blur = cv2.medianBlur(hsv ,11)

lower = {'yellow': (20, 30, 119)}

upper = {'yellow': (54, 255, 255)}

for key, value in upper.items():
    mask = cv2.inRange(blur, lower[key], upper[key])

res = cv2.bitwise_and(image,image, mask= mask)            

cv2.imshow("mask ", mask)
cv2.imshow('stack', np.hstack([image, res]))
cv2.waitKey(0)

#Melhor configuração
# lower = np.array([20, 50, 100])
# upper = np.array([26, 255, 255])

# Teste 1
# lower = np.array([24, 50, 165])
# upper = np.array([26, 255, 255])

# Teste 2
# lower = np.array([20, 50, 100])
# upper = np.array([26, 255, 255])


# Funções uteis

# mostrar imagem = img.show()


# Configuração antiga
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#blur = cv2.medianBlur(hsv ,11)

#lower = np.array([20, 50, 100])
#upper = np.array([26, 255, 255])