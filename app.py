import pickle
from flask import Flask, request, app, jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__,template_folder='template')
regmodel=pickle.load(open("regmodel.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    output=regmodel.predict(np.array(data))
    print(output)
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)