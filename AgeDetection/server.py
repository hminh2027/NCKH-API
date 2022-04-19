import os, sys
from flask import jsonify
import json 
from flask import Flask
from flask import flash, request
from flask import send_from_directory
app = Flask(__name__)

lib_path = os.path.abspath(os.path.join('opencv-age-detection'))
sys.path.append(lib_path)


UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))
    return 'Age Prediction'
#anh

#lay anh ve may client
@app.route('/getID/Image/<filename>',methods=['GET'])
def getIDImage(filename):
	resp= (detect_age.show_Image("images/"+filename, filename))
	return jsonify(resp)
    
import detect_age

#nhan anh tu client
@app.route('/agePrediction',methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        file = request.files['pic']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        x= (detect_age.show_Image("AgeDetection/images/"+filename, filename))
        resp = jsonify('Downloads successfully!')
        resp.status_code = 200
        _json = {'age': x}
       
        r = json.dumps(_json)
        
        return r
        #return jsonify(x)         
    else:
        return "Y U NO USE POST?"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5005", threaded=True, debug = False)
