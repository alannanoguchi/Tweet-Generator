from flask import Flask
import sample
import histogram


app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("sample.txt", "r") as data:
        histo = histogram.histogram_dictionary(data)
    return sample.random_word(histo)