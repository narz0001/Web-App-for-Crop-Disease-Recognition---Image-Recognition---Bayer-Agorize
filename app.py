import os
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
from flask import Flask, render_template, request, redirect, flash
from data_preparation import prepare_data
from ml_models import train_knn_model, train_svc_model, train_rf_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

home = app.root_path

# Mapping of fruits to machine learning models
model_mapping = {
    'Apple': 'svc',
    'Cherry': 'svc',
    'Grape': 'svc',
    'Tomato': 'svc',
    'Peach': 'svc',
    'Strawberry': 'svc',
    'Bellpepper': 'knn',
    'Potato': 'rf',
    'Corn': 'rf'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        fruit_type = request.form['fruit_type']

        # Ensure a valid fruit selection
        if fruit_type not in model_mapping:
            flash('Invalid fruit selection')
            return redirect(request.url)

        # Choose the appropriate fruit based on the selected option
        fruit = fruit_type

        # Get the selected model name
        model_name = model_mapping[fruit_type]

        if model_name:
            # Prepare data based on the selected fruit
            data_input, data_target = prepare_data(f"{home}{os.sep}training{os.sep}", fruit, ['healthy', 'unhealthy'])
            X_train, X_test, y_train, y_test = train_test_split(data_input, data_target, test_size=0.3, random_state=0)

            if model_name == 'svc':
                model = train_svc_model(X_train, y_train)
            elif model_name == 'knn':
                model = train_knn_model(X_train, y_train)
            elif model_name == 'rf':
                model = train_rf_model(X_train, y_train)
            else:
                flash('Invalid model selection')
                return redirect(request.url)

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

            # Predict using the selected model
            prediction = model.predict(reshaped_image)
            y_pred = model.predict(X_test)
            accuracy = f"{accuracy_score(y_test, y_pred) * 100:.2f}%"

            return render_template('result.html', prediction=prediction[0], accuracy_score=accuracy, model_name=model_name)

if __name__ == '__main__':
    app.run(debug=True)
