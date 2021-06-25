import cv2
import numpy as np
from PIL import Image
from glob import glob

# Redimensionar foto
img = Image.open("faixa-horizontal-opencv/fotos/faixa.3.jpg")
img = img.resize((round(400), round(300)), Image.BILINEAR)
img.save( 'faixa-horizontal-opencv/fotos/imagemRedimensionada.jpg', 'JPEG' )

image = cv2.imread("faixa-horizontal-opencv/fotos/imagemRedimensionada.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blur = cv2.medianBlur(hsv ,11)

lower = {'red': (166, 84, 141), 'blue': (97, 100, 117), 'yellow': (17, 59, 119)}

upper = {'red': (186, 255, 255), 'blue': (117, 255, 255), 'yellow': (54, 255, 255) }

for key, value in upper.items():
    kernel = np.ones((9, 9), np.uint8)
    mask_pt = cv2.inRange(blur, lower[key], upper[key])
    mask_pt = cv2.morphologyEx(mask_pt, cv2.MORPH_OPEN, kernel)
    mask_pt = cv2.morphologyEx(mask_pt, cv2.MORPH_CLOSE, kernel)
    if not 'mask' in locals():
        mask = mask_pt
    else:
        mask = mask_pt + mask


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