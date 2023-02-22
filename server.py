# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


app = Flask(__name__)


@app.route('/')
def home():
    message = 'Message sent from backend through to the html file'
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
