!pip install flask
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("G:/Abroad/Durham_AI/Second_SEM/AI in Enterprise system_2004/Lab/fish.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    print(prediction)
    if prediction[0] == 0:
        return render_template('index.html', prediction_text='The flower belong to species Bream')
    elif prediction[0] == 1:
        return render_template('index.html', prediction_text='The flower belong to species Parkki')
    elif prediction[0] == 2:
        return render_template('index.html', prediction_text='The flower belong to species Perch')
    elif prediction[0] == 3:
        return render_template('index.html', prediction_text='The flower belong to species Pike')
    elif prediction[0] == 4:
        return render_template('index.html', prediction_text='The flower belong to species Roach')
    elif prediction[0] == 5:
        return render_template('index.html', prediction_text='The flower belong to species Smelt')
    else:
        return render_template('index.html', prediction_text='The flower belong to species Whitefish')
    


if __name__=='__main__':
    app.run()