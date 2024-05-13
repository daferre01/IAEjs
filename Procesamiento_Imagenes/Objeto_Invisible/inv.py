import cv2 as cv
import numpy as np

data_dir = 'PROGRAMACION_DE_IA/Espacios_de_Color/imagenes/'

def click_raton(event, x, y, flags, param):
    global color_punto
    if event == cv.EVENT_LBUTTONDBLCLK:
        b, g, r = img1[y, x]
        color_punto = np.uint8([[[b, g, r]]])
        color_punto = cv.cvtColor(color_punto, cv.COLOR_BGR2HSV)
        print(f'Click en {x}, {y}, color= {color_punto}')

src1 = cv.VideoCapture(0)
cv.namedWindow('Fondo')

color_punto = None
captura = None

while True:
    ret, img1 = src1.read()

    hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
    if color_punto is not None:
        color_minimo = np.array([color_punto[0, 0, 0] - 10, 10, 10])
        color_maximo = np.array([color_punto[0, 0, 0] + 10, 255, 255])
        mascara = cv.inRange(hsv, color_minimo, color_maximo)
        cv.imshow('Mascara', mascara)
        color_punto = None

    cv.imshow("Objeto", img1)

    if captura is not None:
        alpha = 0.0  # Establece la transparencia a 0 para hacer el objeto completamente invisible
        img_blend = cv.addWeighted(captura, alpha, img1, 1 - alpha, 0)
        cv.imshow('Fondo', img_blend)

    cv.setMouseCallback('Objeto', click_raton)

    if cv.waitKey(10) & 0xFF == 32:
        captura = img1.copy()

    if cv.waitKey(10) & 0xFF == 27:
        break

src1.release()
cv.destroyAllWindows()

