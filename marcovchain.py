from dictogram import Dictogram
corpus = "one fish two fish blue fish red fish"

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

print(markovhistogram(words))