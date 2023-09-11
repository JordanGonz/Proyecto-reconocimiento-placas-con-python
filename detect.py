import cv2
import numpy as np
import os

net = cv2.dnn.readNet('detector.cfg', 'modelo.weights', 'darknet')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

classes = ["placa"]
colors = [(0, 255, 0)] 

 
conf_threshold = 0.5
if not os.path.exists('objetos_encontrados'):
    os.makedirs('objetos_encontrados')

objetos_capturados = []

while True:
    ret, frame = cap.read()  
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getUnconnectedOutLayersNames()
    outs = net.forward(layer_names)
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > conf_threshold:
                class_name = classes[class_id]
                color = colors[class_id]

                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                x = int(center_x - width / 2)
                y = int(center_y - height / 2)

                # Verificar si un objeto similar ya ha sido capturado
                objeto_similar = False
                for obj in objetos_capturados:
                    if abs(x - obj[0]) < 20 and abs(y - obj[1]) < 20:
                        objeto_similar = True
                        break

                if not objeto_similar:
                    objetos_capturados.append((x, y))

                 

                    cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)
                    objeto_img = frame[y:y+height, x:x+width]
                    cv2.imwrite('objetos_encontrados/objeto_{}.jpg'.format(len(objetos_capturados)), objeto_img)
    cv2.namedWindow('Detección', cv2.WINDOW_NORMAL)
    cv2.imshow('Detección', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
