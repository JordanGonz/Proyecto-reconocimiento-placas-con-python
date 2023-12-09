from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/image/count')
def get_image_count():
    return str(len(os.listdir('objetos_encontrados')))
@app.route('/image/execute')
def get_image_execute():
    return str(len(os.listdir('objetos_encontrados')))
@app.route('/images/<path:filename>')
def get_image(filename):    
    try:
        return send_file(os.path.join('objetos_encontrados', filename))
    except:
        return 'Image not found', 404
    
if __name__ == '__main__':
    app.run()
