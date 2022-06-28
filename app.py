from flask import Flask,render_template, request


app = Flask(__name__)



@app.route('/')
def face():
  if request.method == 'POST':
   img = request.method['img']

   #b = bytes(img, 'utf-8')
   #print(b)
   #image= b[b.find(b'/9'):]
  return render_template('fc.html')

if __name__ == '__main__':
 app.run()