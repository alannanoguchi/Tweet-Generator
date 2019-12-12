from dictogram import Dictogram
corpus = "one fish two fish blue fish red fish"

words = corpus.split() #split the corpus into individual words
# pairs = [words[i]+' '+words[i+1] for i in range(len(words)-1)]
# print(pairs)


for i in range(len(words) -1):
    first_word = words[i]
    second_word = words[i+1]
    pairs = (first_word, second_word)
    # print(pairs)
    big_dict ={}
    # marcov_dict = {}  # can't use a regular dict
    marcov_dict = Dictogram()  # to use a dictogram method (add_count), we must first establish a Dictogram() object
    marcov_dict.add_count(second_word)
    # print(marcov_dict)

    big_dict[first_word] = marcov_dict
    if first_word not in big_dict.keys():
        big_dict.get(first_word).add_count(second_word)
    else:
        big_dict[first_word].append(second_word)
    print(big_dict)

