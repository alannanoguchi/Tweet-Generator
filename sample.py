import random
from histogram import histogram_dictionary, all_words # import the histogram_dictionary function from the histogram file

def random_word(histo):

    word_list = histo # this variable contains all of the words from the histogram
    words = list(word_list) # this is a list of of the words form the histogram
    word_index = (random.randint(0, len(histo) - 1)) # return a random choice from the histogram 
    word_list = words[word_index] 

    return word_list


def probability(histo):
    """ equation for probability = (num of occurances) / sample total
        Take the value of a word. Divide it by the total length of the histogram. 
        Mulitply by 100 to get percentage.
        Be able to show all of the words and their percent in a list. """

    total_count = len(histo.values()) # this is the total number of items in the histo. Should be 61.
    # print(total_count) # yes, 61
    word_percents = {}
    for key in histo: # for the key in the histogram
        word_percents[key] = str(round(histo[key] / total_count * 100, 2)) + "%" # divide it by the total items in the histogram and divide by 100
        # round(_, which decimal point) <--- this will round the number to the second decimal point

    return word_percents
    # print(word_percents)
    
    

    
    



if __name__ == '__main__':

    with open("sample.txt", "r") as data:
        histo = histogram_dictionary(data)
        random_word(histo)
        probability(histo)