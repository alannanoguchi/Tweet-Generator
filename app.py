from flask import Flask, render_template
import sample
import histogram, markovchain
from dictogram import Dictogram
from markovchain import random_walk_second_order, markov_second_order
from re import sub, split

app = Flask(__name__)

# file = corpus.txt
# text = load_text(text)
# clean_text = remove_names(text)


# @app.route('/')
# def hello_world():
#     with open("sample.txt", "r") as data:
#         histo = histogram.histogram_dictionary(data)
#     return sample.random_word(histo)
#   Regexp for Character names:  


# corpus = "MEREDITH: That fantasy of what your life would be. White dress, Prince Charming, who'd carry you away to a castle on a hill. You\'d lie in bed at night and close your eyes, and you had complete and utter faith. Eight hours, 1 6 ounces of chocolate and 32 cupcakes, and they still don\'t taste right. No, these are good. Martha Stewart would be proud. Yeah, look where it got her."
def load_text(filename):
    '''Reads file data, converts all words to lowercase, strips starting & trailing punctuation and splits words into a list'''
    with open(filename, 'r') as f:
        read_data = f.read()
    return read_data  


def remove_names(corpus):
    regex = '([A-Z])+(.+?)\\:'
    remove_chars = sub(regex, " ", corpus)
    return remove_chars

file = "corpus.txt"
text = load_text(file)
clean_text = remove_names(text)

words = split(r'\s', clean_text) #split the corpus into individual words
# pairs = [words[i]+' '+words[i+1] for i in range(len(words)-1)]
# print(pairs)


@app.route('/')
def index():
    """Return homepage."""
    # with open("sample.txt", "r") as data:
    #     histo = histogram.histogram_dictionary(data)
    #     word = sample.random_word(histo)
    markov =  markov_second_order(words)
    random_sent = random_walk_second_order(markov)
 
    return render_template('index.html', random_sent = random_sent)



if __name__ == '__main__':
  app.run(debug=True)
 