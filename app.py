from flask import Flask

app = Flask(__name__)

def front_end():
    print(f"Choose the Type of Fruit:"
          f"1. Apple - 1"
          f"2. Bellpepper - 2"
          f"3. Cherry - 3"
          f"4. Corn - 4"
          f"5. Grape - 5"
          f"6. Potato - 6"
          f"7. Tomato - 7"
          f"8. Peach - 8"
          f"9. Strawberry - 9")

#Takes Input based on the options and returns the appropriate Fruit Type
def returnOptionSelected():




@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
