"""For Install Library Write all Library Name under
requirements.txt file--->Go to Terminal--->pip install
-r requirements.txt"""
import pickle
from flask import Flask,request,jsonify,render_template
# render_template is responsible for finding the URL of the HTML File
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

# This line is important for CSS File Loading and Background Image Loading
app.static_folder='static'
cors=CORS(app)

## import ridge regresor model and standard scaler pickle
## Open Pickle model in Read byte Mode
knn_model=pickle.load(open('models/knn.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

## Route for home page
# Create a Home Page
@app.route('/')
def index():
    return render_template('index.html')

''' Create "index.html", After writing upto that go to terminal and write "python application.py"'''

'''1. The GET method is used to request data from a specified resource.
   2. When a form is submitted using the GET method, the form data is appended to the URL in the form of query parameters.
   3. This method is suitable for forms with a small amount of data, and the data is visible in the URL.'''

'''1. The POST method is used to submit data to be processed to a specified resource.
   2. When a form is submitted using the POST method, the form data is sent in the body of the HTTP request, not as part of the URL.
   3. This method is suitable for forms with larger amounts of data or when sensitive information, such as passwords, is being transmitted.'''  

'''In summary, use the GET method when you want to retrieve data, and use the POST method when you want to send data to be processed
 on the server. The choice between them depends on the nature of the data being transmitted and the security considerations.'''

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        # request.form.get(' "Name" of The field given in the Form')
        # Name Should be Exactly Match
        Ia = float(request.form.get('Ia'))
        Ib = float(request.form.get('Ib'))
        Ic = float(request.form.get('Ic'))
        Va = float(request.form.get('Va'))
        Vb = float(request.form.get('Vb'))
        Vc = float(request.form.get('Vc'))
        
        # Order of "Ia,Ib,Ic,Va,Vb,Vc" are Important
        new_data_scaled=standard_scaler.transform([[Ia,Ib,Ic,Va,Vb,Vc]])
        result=knn_model.predict(new_data_scaled)
        
        
    
        return render_template('fault.html',result=result[0])
        
    else:
        return render_template('fault.html')

        
        
    

''' Host Address, When we give By dafault Host address to "0.0.0.0", This is basically Map to Local
IP Address of any Machine that we are working, Generallly Local Ip address are not publically Available
The IP Address where this code are exactly running are "//127.0.0.1:5000", Address we can generally collect
by running the HTML Application on Local Server'''

if __name__=="__main__":
    app.run(host="0.0.0.0")


# First Load this Load by "python application.py" in Terminal
# After That Go to the Link by Local Server or by direct Link Copy Paste.    

