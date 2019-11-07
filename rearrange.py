import sys, random


def random_order(params):
    words_list = params
    random_words_list = []

    # while the length of the random words list is less than the words list, a random word is chosen from the params
    while len(random_words_list) < len(words_list):
        random_word = random.choice(params)
        
        # if the random word is not in the random words list, then add it to the random words list
        if random_word not in random_words_list: # removes the word so it cannot be chosen again
            random_words_list.append(random_word)

    random_sentence = " ".join(random_words_list) # this will take the words in the list and return a sentence
    print(random_sentence)




if __name__ == "__main__":
    params = sys.argv[1:]
    random_order(params)