from flask import Flask, render_template
import sample
import histogram, markovchain
from dictogram import Dictogram
from markovchain import random_walk, markovhistogram


app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     with open("sample.txt", "r") as data:
#         histo = histogram.histogram_dictionary(data)
#     return sample.random_word(histo)

corpus = "That fantasy of what your life would be. White dress, Prince Charming, who'd carry you away to a castle on a hill. You\'d lie in bed at night and close your eyes, and you had complete and utter faith.[sighs.]Eight hours, 1 6 ounces of chocolate and 32 cupcakes, and they still don\'t taste right. No, these are good. Martha Stewart would be proud. Yeah, look where it got her."

words = corpus.split() #split the corpus into individual words
# pairs = [words[i]+' '+words[i+1] for i in range(len(words)-1)]
# print(pairs)


@app.route('/')
def index():
    """Return homepage."""
    # with open("sample.txt", "r") as data:
    #     histo = histogram.histogram_dictionary(data)
    #     word = sample.random_word(histo)
    markov = markovhistogram(words)
    random_sent = random_walk(words, markov)
 
    return render_template('index.html', random_sent = random_sent)



if __name__ == '__main__':
  app.run(debug=True)