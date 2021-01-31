from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
      app.debug = True
else:
      app.debug = False

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/<data>')
def dashboard(data):
   return render_template('2nd.html')

@app.route('/<data1>//<data2>')
def dashboard1(data1, data2):
   return render_template('3rd.html')

@app.route('/total', methods=['POST'])
def total1(text1=0, text2=0):
      if request.method =='POST':
            text1 = request.form['text1']
            text2 = request.form['text2']
            print(text1, text2)
            return redirect(url_for('dashboard1',data1 = text1, data2 = text2))

@app.route('/sum', methods=['POST'])
def sum1():
      if request.method =='POST':
            text10 = request.form['text10']
            print(text10)
            return redirect(url_for('dashboard',data = text10))



if __name__ == '__main__':
      app.debug = True
      app.run()