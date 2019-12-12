from dictogram import Dictogram 
from random import choice

corpus = "That fantasy of what your life would be. White dress, Prince Charming, who'd carry you away to a castle on a hill. You\'d lie in bed at night and close your eyes, and you had complete and utter faith.[sighs.]Eight hours, 1 6 ounces of chocolate and 32 cupcakes, and they still don\'t taste right. No, these are good. Martha Stewart would be proud. Yeah, look where it got her."

words = corpus.split() #split the corpus into individual words
# pairs = [words[i]+' '+words[i+1] for i in range(len(words)-1)]
# print(pairs)


def markovhistogram(words):
    """Create a histogram for a markov chain"""
    big_dict ={}

    for i in range(len(words) -1):
        first_word = words[i]
        second_word = words[i+1]
        # pairs = (first_word, second_word)
        # print(pairs)

        # big_dict[first_word] = marcov_dict
        if first_word not in big_dict.keys():
            histo = []
            big_dict[first_word] = histo
            
        big_dict[first_word].append(second_word)
         
    values = big_dict.items()
    for key, value in values:
        # marcov_dict = {}  # can't use a regular dict
        big_dict[key] = Dictogram(value)  # to use a dictogram method (add_count), we must first establish a Dictogram() object
        # marcov_dict.add_count(second_word)
        # print(marcov_dict)
    return big_dict

# print(markovhistogram(words))

def random_walk(words, markov):
    """Use a random word from the big_dict to "walk" around the marcov chain to create a sentence"""
    sentence = [] # add all of the words to this list to create a sentence
    random_key = [key for key in markov.keys()]

    i = 0
    while i < 5:
        output = choice(random_key)
        sentence.append(output)
        i += 1

    return " ".join(sentence)
markov = markovhistogram(words)
print(random_walk(words, markov))
