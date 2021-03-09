import time
import random
import numpy as np
from flask import Flask, render_template, redirect, url_for
from test_list import tests

# Flask
app = Flask(__name__)

test = np.random.rand()
# Routes
@app.route('/')
def base():
    return render_template('base.html', test=test)


@app.route('/start', methods=["POST"])
def start_tests():
    global test
    test = np.random.rand()


if __name__ == "__main__":
    app.run(debug=True)
