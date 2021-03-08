import random
import serial
import time
from flask import Flask, render_template
from test_list import tests

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
