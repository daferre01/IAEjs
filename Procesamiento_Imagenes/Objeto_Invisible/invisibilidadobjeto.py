import cv2 as cv
import numpy as np

color_seleccionado_hsv = None
rango_hsv_inferior = None
rango_hsv_superior = None
capa_objeto = None
frame_inicial = None

def procesar_doble_click(event, x, y, flags, param):
    global color_seleccionado_hsv, rango_hsv_inferior, rango_hsv_superior, capa_objeto
    if event == cv.EVENT_LBUTTONDBLCLK:
        color_seleccionado_hsv = obtener_color_hsv(x, y)
        establecer_rangos_hsv(color_seleccionado_hsv)
        capa_objeto = frame_actual
        print(f"Rango de Color HSV Seleccionado: {rango_hsv_inferior} - {rango_hsv_superior}")

def obtener_color_hsv(x, y):
    b, g, r = frame_actual[y, x]
    color_bgr = np.uint8([[[b, g, r]]])
    return cv.cvtColor(color_bgr, cv.COLOR_BGR2HSV)

def establecer_rangos_hsv(color_hsv):
    global rango_hsv_inferior, rango_hsv_superior
    rango_hsv_inferior = np.array([color_hsv[0, 0, 0] - 10, 10, 10])
    rango_hsv_superior = np.array([color_hsv[0, 0, 0] + 10, 255, 255])

def capturar_frame_inicial():
    global frame_inicial
    if frame_inicial is None:
        mostrar_frame("Invisible", frame_actual)
        frame_inicial = frame_actual

def procesar_capa_objeto():
    global capa_objeto, frame_inicial, rango_hsv_inferior, rango_hsv_superior, frame_actual_hsv
    if capa_objeto is not None and frame_inicial is not None:
        frame_actual_hsv = cv.cvtColor(frame_actual, cv.COLOR_BGR2HSV)
        objeto_en_mascara = aplicar_mascara(frame_actual, obtener_mascara_negra())
        frame_inicial_en_mascara = aplicar_mascara(frame_inicial, obtener_mascara_blanca())
        resultado_final = cv.add(objeto_en_mascara, frame_inicial_en_mascara)
        mostrar_frame("Resultado Procesado", resultado_final)

def obtener_mascara_negra():
    return cv.inRange(obtener_mascara_blanca(), 0, 128)

def obtener_mascara_blanca():
    return cv.inRange(frame_actual_hsv, rango_hsv_inferior, rango_hsv_superior)

def aplicar_mascara(imagen, mascara):
    return cv.bitwise_and(imagen, imagen, mask=mascara)

def mostrar_frame(nombre_ventana, frame):
    cv.namedWindow(nombre_ventana)
    cv.imshow(nombre_ventana, frame)

captura_video = cv.VideoCapture(1)
cv.namedWindow("Ventana de Salida")
cv.setMouseCallback("Ventana de Salida", procesar_doble_click)

while True:
    ret, frame_actual = captura_video.read()

    if ret:
        frame_actual = cv.flip(frame_actual, 1)
        mostrar_frame("Ventana de Salida", frame_actual)

    tecla = cv.waitKey(10)
    
    if tecla == 27:  
        break

    if tecla == 32:  
        capturar_frame_inicial()

    procesar_capa_objeto()

captura_video.release()
cv.destroyAllWindows()
