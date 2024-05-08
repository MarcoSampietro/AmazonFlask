from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('amazon.html')

@app.route('/elenco')
def elenco():
    return 

@app.route('/prodotto')
def prodotto():
    return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)