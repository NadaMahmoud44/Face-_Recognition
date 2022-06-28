from flask import Flask,render_template, request
from main import *
import face_recognition as fr


app = Flask(__name__)



@app.route('/')
def face():
  if request.method == 'POST':
    load_image = request.method['img']
    target_image = fr.load_image_file(load_image)
    target_encoding = fr.face_encodings(target_image)
    find_target_face()




   #b = bytes(img, 'utf-8')
   #print(b)
   #image= b[b.find(b'/9'):]
  return render_template('fc.html')

if name == '__main__':
 app.run()
