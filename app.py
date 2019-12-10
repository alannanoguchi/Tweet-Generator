from flask import Flask, render_template
import sample
import histogram


app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     with open("sample.txt", "r") as data:
#         histo = histogram.histogram_dictionary(data)
#     return sample.random_word(histo)


@app.route('/')
def index():
    """Return homepage."""
    with open("sample.txt", "r") as data:
        histo = histogram.histogram_dictionary(data)
        word = sample.random_word(histo)
    return render_template('index.html', word = word)



if __name__ == '__main__':
  app.run(debug=True)