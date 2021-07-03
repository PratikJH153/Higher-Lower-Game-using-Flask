from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess the Number between 0 and 9</h1>' \
           '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def guess_number(number):
    if number > random_number:
        return '<h1 color = "purple">Too High Try Again!</h1>' \
               '<img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < random_number:
        return '<h1 color = "red">Too Low Try Again!</h1>' \
               '<img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 color = "green">You Found Me!</h1>' \
               '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
