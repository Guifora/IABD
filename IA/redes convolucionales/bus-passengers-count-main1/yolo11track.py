import cv2
from tracker1 import ObjectCounter  # Importar ObjectCounter desde tracker.py

# Definir la función de callback del mouse
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  # Verificar si el mouse se mueve
        point = [x, y]
        print(f"El mouse se movió a: {point}")

# Abrir el archivo de video
cap = cv2.VideoCapture('/home/iabd/Documentos/IABD/IABD/IA/redes convolucionales/bus-passengers-count-main/1.mp4')

# Definir los puntos de la región para el conteo de objetos
region_points = [(386, 103), (458, 499)]

# Inicializar el contador de objetos
counter = ObjectCounter(
    region=region_points,  # Pasar los puntos de la región
    model="yolo11s.pt",  # Modelo utilizado para el conteo de objetos
    classes=[0],  # Detectar solo la clase "persona"
    show_in=True,  # Mostrar el conteo de entradas
    show_out=True,  # Mostrar el conteo de salidas
    line_width=2,  # Ajustar el grosor de la línea de visualización
)

# Crear una ventana con nombre y asignar la función de callback del mouse
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

count = 0  # Contador de fotogramas

while True:
    # Leer un fotograma del video
    ret, frame = cap.read()
    if not ret:
        break  # Si el video termina, salir del bucle
        # Para reiniciar el video desde el principio, descomenta las siguientes líneas:
        # cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # continue

    count += 1
    if count % 2 != 0:  # Saltar los fotogramas impares para mejorar el rendimiento
        continue

    # Redimensionar el fotograma a 1020x500 píxeles
    frame = cv2.resize(frame, (1020, 500))

    # Procesar el fotograma con el contador de objetos
    frame = counter.count(frame)

    # Mostrar el fotograma procesado
    cv2.imshow("RGB", frame)
    
    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar el objeto de captura de video y cerrar la ventana de visualización
cap.release()
cv2.destroyAllWindows()
