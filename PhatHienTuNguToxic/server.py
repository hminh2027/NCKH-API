from flask import Flask 
from flask import jsonify
import json
import os.path
from flask import request    
app = Flask(__name__)


#Goi cac thu vien
import demo1

@app.route('/toxicDetection/<text>',methods=['GET', 'POST'])
def detection(text):
    return demo1.detection(text)

@app.route('/')
def home():
    return 'Toxic Detection API!'

if __name__ == '__main__':
        app.run(debug=True, host= '0.0.0.0', port='9999')
        #app.run()





























