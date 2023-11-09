import os

from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize

from flask import Flask, render_template, request, redirect, flash
from data_preparation import prepare_data
from ml_models import train_knn_model, evaluate_knn_model

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

home = app.root_path
fruit = 'bellpepper'
categories = ['healthy', 'unhealthy']

data_input, data_target = prepare_data(f"{home}{os.sep}training{os.sep}", fruit, categories)
knn_model = train_knn_model(data_input, data_target)

# Sample test data (replace this with the actual test data)
X_test, y_test = prepare_data(f"{home}{os.sep}training{os.sep}", fruit, categories)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # Sample test data preparation for the uploaded file
        uploaded_image = io.imread(file)
        resize_img = resize(uploaded_image, (200, 200))
        gray_image = rgb2gray(resize_img)
        flattened_image = gray_image.flatten()

        # Reshape the image to match the training data
        reshaped_image = flattened_image.reshape(1, -1)

        # Predict using the KNN model
        prediction = knn_model.predict(reshaped_image)
        flash(prediction)
        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)