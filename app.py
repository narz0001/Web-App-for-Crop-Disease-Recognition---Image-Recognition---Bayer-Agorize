from flask import Flask, render_template, request, redirect, flash
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Map fruit types to machine learning models
fruit_models = {
    'Apple': 'apple_model_function',
    'Bellpepper': 'bellpepper_model_function',
    'Cherry': 'cherry_model_function',
    'Corn': 'corn_model_function',
    'Grape': 'grape_model_function',
    'Peach': 'peach_model_function',
    'Potato': 'potato_model_function',
    'Strawberry': 'strawberry_model_function',
    'Tomato': 'tomato_model_function'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def apple_model_function(image_path):
    return f'Apple Model Result for {image_path}'

def bellpepper_model_function(image_path):
    return f'Bellpepper Model Result for {image_path}'

def cherry_model_function(image_path):
    return f'Cherry Model Result for {image_path}'

def corn_model_function(image_path):
    return f'Corn Model Result for {image_path}'

def grape_model_function(image_path):
    return f'Grape Model Result for {image_path}'

def peach_model_function(image_path):
    return f'Peach Model Result for {image_path}'

def potato_model_function(image_path):
    return f'Potato Model Result for {image_path}'

def strawberry_model_function(image_path):
    return f'Strawberry Model Result for {image_path}'

def tomato_model_function(image_path):
    return f'Tomato Model Result for {image_path}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    fruit_type = request.form['fruit_type']

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Check if the selected fruit has a corresponding model
        if fruit_type in fruit_models:
            # Get the corresponding model function
            model_function = globals()[fruit_models[fruit_type]]
            # Run the model function with the uploaded image path
            result = model_function(filename)
            return result
        else:
            flash('Invalid fruit type selected.')
            return redirect(request.url)

    else:
        flash('Invalid file format. Please upload a valid image file.')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
