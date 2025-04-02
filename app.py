from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
import os
import shutil

# Function to copy image from local system to static folder
def copy_image_to_static(source_path, member_name):
    try:
        # Create static/images directory if it doesn't exist
        static_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
        os.makedirs(static_dir, exist_ok=True)
        
        # Get file extension from source
        _, ext = os.path.splitext(source_path)
        
        # Create destination path
        dest_path = os.path.join(static_dir, f"{member_name}{ext}")
        
        # Copy the file
        shutil.copy2(source_path, dest_path)
        print(f"Successfully copied image for {member_name}")
        return True
    except Exception as e:
        print(f"Error copying image: {str(e)}")
        return False

# Load the trained ML model
model_path = os.path.join(os.path.dirname(__file__), "water_potability_model.pkl")
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__, static_folder='static')

# Example usage - add your local image paths here
team_images = {
    'shobhit': r"C:\Users\KIIT\Pictures\IMG-20230218-WA0009.jpg",  # Your actual path
    'yashwardhan': "",  # Add path for Yashwardhan's photo
    'ankit': "",        # Add path for Ankit's photo
    'harsh': "",        # Add path for Harsh's photo
    'priyanka': "",     # Add path for Priyanka's photo
    'aadi': ""         # Add path for Aadi's photo
}

# Copy all team member images
for member, image_path in team_images.items():
    if image_path:  # Only copy if path is provided
        copy_image_to_static(image_path, member)

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
