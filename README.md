Water Potability Prediction App

This project is a Machine Learning-based Water Potability Prediction App that determines whether water is safe to drink based on key parameters. The model uses pH, Hardness, and Sulfate levels to make predictions.

Features

Predicts water potability using a trained ML model.

Uses only three essential water quality features for simplicity.

Cloud-based API deployment using Flask.

Technologies Used

Python (Machine Learning & API development)

Flask (Backend API)

Scikit-Learn (ML model training & prediction)

Installation

Backend (Flask API)

Clone this repository:

git clone https://github.com/lucifer9973/water-quality-app.git
cd water-quality-app

Install dependencies:

pip install -r requirements.txt

Run the Flask API:

python app.py

Usage

Enter water quality parameters (pH, Hardness, Sulfate).

Click Predict to get the potability result.

The model will return whether the water is potable or not potable.

Deployment

You can deploy the Flask API on a cloud platform like Heroku, AWS, or Google Cloud for real-time predictions.

Contributing

Feel free to contribute by submitting issues or pull requests!
