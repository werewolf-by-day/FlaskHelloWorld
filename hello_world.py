from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def welcome():
    return 'Welcome to my portfolio! My name is Jason'

@app.route('/hello')

def helloWorld():
    return render_template('/hello.html')
app.run(debug=True)
