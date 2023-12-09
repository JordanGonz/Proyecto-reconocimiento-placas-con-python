import os
import cv2
import pytesseract
import re
import requests
import datetime
import random
import flask 


os.environ['TESSDATA_PREFIX'] = 'C:\\Program Files\\Tesseract-OCR\\\\tessdata'
# Path de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

directory = 'objetos_encontrados'

urlApi = 'http://localhost:3000/multas/multar'


files = os.listdir(directory)
if __name__ == '__main__':

    all_text = '' 

    placas = []
    for file in files:
        img = cv2.imread(os.path.join(directory, file))
        img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
        gray = cv2.GaussianBlur(gray, (3, 3), 0)  
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        dilate = cv2.dilate(thresh, kernel, iterations=1)

        text = pytesseract.image_to_string(dilate, lang='eng', config='--psm 6')
        text = re.sub(r'ECUADOR', '', text)
        text = re.sub(r'eouapor', '', text)
        text = re.sub(r'RUADOR', '', text)
        text = re.sub(r'ecuanor', '', text)
        text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
        text = text.replace(" ", "")
        placas.append(text)
        
   
    all_text = ' '.join(placas)
    #url = f'http://localhost:3000/propietario?placa={placa}'

    with open('placas.txt', mode='w', encoding='utf-8') as file:
        for placa in placas:
            #request = requests.get(url)
        
            digitos = re.findall(r'\d', placa)

         
            last_digit = int(digitos[-1]) if digitos else None
            print (last_digit)

            #list_correos = ['luis@example.com', 'andres@example.com','jordan@example.com','guido.25@hotmail.com']
            
           # correo = random.choice(list_correos)


            now = datetime.datetime.now()
            weekday = now.weekday()  
            last_digit_perday = {
                0: [1, 2],
                1: [8, 2],
                2: [5, 6],
                3: [7, 8],
                4: [9, 0],
                5: [],
                6: []
            }
        

            
            data = {
                'placa': placa,
                'motivo': 'circulacion en horario no permitido',
                
            }

            hour = now.hour
            print(last_digit_perday[weekday])
            if last_digit not in last_digit_perday[weekday] or ((5 <= hour <= 10) or (16 <= hour <= 21)):
                print('El vehículo con placa {} no puede circular en este momento.'.format(placa))
                response = requests.post(urlApi,json=data,verify=False)
                file.write('El vehículo con placa {} no puede circular en este momento.\n'.format(placa))
            else:
                print('El vehículo con placa {} puede circular en este momento.'.format(placa))
                file.write('El vehículo con placa {} puede circular en este momento.\n'.format(placa))
