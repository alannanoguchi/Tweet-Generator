from dictogram import Dictogram 
from random import choice, randint

corpus = "That fantasy of what your life would be. White dress, Prince Charming, who'd carry you away to a castle on a hill. You\'d lie in bed at night and close your eyes, and you had complete and utter faith. Eight hours, 1 6 ounces of chocolate and 32 cupcakes, and they still don\'t taste right. No, these are good. Martha Stewart would be proud. Yeah, look where it got her."

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
    """Use a random word from the big_dict to "walk" around the markov chain to create a sentence"""
    sentence = [] # add all of the words to this list to create a sentence
    random_key = [key for key in markov.keys()]
    # print(random_key)

    i = 0
    while i < 5:
        output = choice(random_key)
        # psrint(output)
        sentence.append(output)
        i += 1

    return " ".join(sentence)

# markov = markovhistogram(words)
# print(random_walk(words, markov))



def markov_second_order(words):
    big_dict ={}

    for i in range(len(words) -2):
        first_word = words[i]
        second_word = words[i +1]
        # pairs = (first_word, second_word)
        # print(pairs)
        third_word = words[i + 2]
        # big_dict[first_word] = marcov_dict
        if first_word not in big_dict.keys():
            histo = []
            big_dict[(first_word, second_word)] = histo
            
            
        big_dict[(first_word, second_word)].append(third_word)
         
    values = big_dict.items()
    for key, value in values:
        # marcov_dict = {}  # can't use a regular dict
        big_dict[key] = Dictogram(value)  # to use a dictogram method (add_count), we must first establish a Dictogram() object
        # marcov_dict.add_count(second_word)
        # print(marcov_dict)
    return big_dict
    # print(big_dict)

# print(markov_second_order(words))  


def random_walk_second_order(markov):
    """Create a list of tupled words to choose from. Randomly choose a first tuple which includes{(first_word[0], second_word[1])}. Create another tuple which includes the {(second_word[1], next_word)}. The next_word is a sample word. Create a while loop to iterate through the histogram until set number of times. Append the next_word to the sentence"""

    sentence = []
    all_keys = [key for key in markov.keys()]
    random_key = choice(all_keys)
    # print(random_key)
    # i = 
    first_tuple = (random_key[0], random_key[1])
    # print(markov)
    # print ("First tuple: " + str(first_tuple))
    sentence.append(random_key[0])
    sentence.append(random_key[1])
    # print (sentence)

    get_histo = markov.get(first_tuple, 'not found')
    # print("Print get_histo: " + str(get_histo))
    # print(get_histo)
 
    sampled_word = get_histo.sample()
    sentence.append(sampled_word)
    # print(sentence)

    next_tuple = (first_tuple[1], sampled_word)
    # print ("Next tuple: " + str(next_tuple))

    next_word = markov.get(next_tuple, 'not found')
    # print(next_word)

    i = 2
    while i < 10:
        # output = choice(random_key)
        

        # if sampled_word in sentence:
            
        #     next_tuple = (first_tuple[1], sampled_word)
        #     sentence.append(next_word)
        #     i += 1
        get_histo = markov.get(next_tuple, 'not found')
        sampled_word = get_histo.sample()
        sentence.append(sampled_word)
        next_tuple = (next_tuple[1], sampled_word)
        i += 1
    
    return " ".join(sentence)
    # sentence = []
    # i = randint(0, len(words) -1)
    # random_key = (words[i], words[i + 1])

    # while len(sentence) < 10:
    #     output = choice(words)
    #     sentence.append(output)
    # return " ".join(sentence)



# markov = markovhistogram(words)
markov = markov_second_order(words)
print(random_walk_second_order(markov))

