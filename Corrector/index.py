from autocorrect import Speller
import cv2
from pyzbar import pyzbar



corrector = Speller(lang='es')

def corregir_palabra(palabra: str):
    if not corrector(palabra) == palabra:
        return corrector(palabra)
    else:
        return palabra

try:
    # Inicializo la camara
    cap = cv2.VideoCapture(0)
    # Mientras este abierta, ret es true si lee correctamente
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Decodifico los codigos de barras y lo guarda en la variable barcodes
        barcodes =pyzbar.decode(frame)

        # Dibujo el rectangulo en las coordenadas donde se encuentra el codigo y superpongo el valor en la posicion 
        for barcode in barcodes:
            (x,y,w,h) = barcode.rect
            cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0),2)
            barcode_value = barcode.data.decode("utf-8")
            cv2.putText(frame,barcode_value,(x,y -10),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,255,0),2)
            print(barcode_value)
        cv2.imshow('Barcode Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    #Liberar recursos
    cap.release()
    cv2.destroyAllWindows()