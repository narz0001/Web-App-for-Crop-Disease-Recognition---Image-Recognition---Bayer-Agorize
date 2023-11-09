from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['fruit_choice']

    if user_input.isdigit() and 1 <= int(user_input) <= 9:
        return f"You chose fruit number {user_input}"
    else:
        return "Invalid input. Please enter a number between 1 and 9."


if __name__ == '__main__':
    app.run()