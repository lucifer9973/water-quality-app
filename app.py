from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
import os
import shutil

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all form data
        form_data = request.form.to_dict()
        
        # Extracting input values from form
        features = [float(value) for value in form_data.values()]
        input_data = np.array([features])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Potable" if prediction == 1 else "Not Potable"
        
        return render_template('index.html', 
                             prediction_text=f'Water Quality: {result}',
                             form_data=form_data)
    except Exception as e:
        return render_template('index.html', 
                             prediction_text=f'Error: {str(e)}',
                             form_data=request.form.to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
