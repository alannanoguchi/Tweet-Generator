import os  # if you are messing with files ouside of the actual app, you have to import os
import re


def all_words(source_text):
    text =  open("sample.txt", "r") # This opens the text file (either sample text or iliad text)
    all_words = text.read() # this reads the file 
    remove_chars = re.sub(r"[^a-z0-9]"," ", all_words.lower()) # this will remove the special characters from the text and every word will be read as lowercase 
    words_list = remove_chars.split(' ') # split the words at each sapce and add to list 
    return words_list



def histogram_dictionary(source_text):
    """Reads source_text and returns a dictionary (as a histogram) of the words"""
    histogram = {}

    words = all_words(source_text) # these are the words that were formated from the function all_words

    for word in words: # for a word in the list of words
        if word in histogram: # if the word is in the histogram...
            histogram[word] = histogram.get(word, 0) + 1  # the value increases by 1
        else: # if the word is not in the histogram
            histogram[word] = 1 # it is added to the histogram with a value of 1
    return histogram

    # for line in lines:
    #     line = re.sub(r"[^a-z0-9]"," ",line.lower())
    #     words = line.split(' ')
    #     for word in words:
            
    #         if word in histogram:
    #             histogram[word] = histogram.get(word, 0) + 1
    #         else:
    #             histogram[word] = 1
    # return histogram
    # print(histogram)
        
        

def unique_words(source_text):

    histogram = {}

    words = all_words(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
        
    return len(histogram) # return the length of the histogram 
    # print(len(histogram))


def frequency(word, histogram):
    # TODO: create a function that takes a word and histogram argument and returns the number of times that word appears in a text
    
    print (histogram.get(word, "Word is not in list")) 
    # return the value of the word that is searched, if the input is not in the list then the message will show
    
   

def list_of_lists(source_text): # elements in a list are mutable, enclosed in square brackets
    words = all_words(source_text)

    histogram = []
    new_hist_list = []

    # this creates a list:
    for words in words: # for word in the source_text
        if words in histogram: # if the word is in the histogram
            word_index = histogram.index(words) # the word is added to an index which has all the words
            histogram[word_index + 1] += 1 # when the word appears again, the value of it goes up by one
        else: # if the word is not already there
            histogram.append(words) # the word is added to the list
            histogram.append(1) # the word is given a value of one

    # this creates a sublist within the above list
    for item in range(0, len(histogram), 2):
        new_hist_list.append([histogram[item], histogram[item+1]])        

    # print(new_hist_list)
    return new_hist_list

def tuples(source_text): # elements in a tuple are immutable, faster to iterte over, enclosed in parenthesis
    
    histogram = list_of_lists(source_text)
    new_tuples_list = []

    for x in histogram: # for a item x in the histogram
        new_tuples_list.append(tuple(x)) # add it to a new sublist of tuples
        
    # print(new_tuples_list)
    return new_tuples_list

    



if __name__ == '__main__':

    with open("sample.txt", "r") as data:
        histo = histogram_dictionary(data)
        unique_words(histogram_dictionary)
        frequency("is", histo)
        list_of_lists(data)
        tuples(data)
    
   