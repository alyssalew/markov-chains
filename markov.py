"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    our_file = open(file_path)
    #print our_file.read()
    return our_file.read()
    #string_of_file = str(file_path)


    



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    # Put str into liist
    words = text_string.split()
    print words
    #create an empty tuple
    word_pair = tuple()
    set_of_tuples = set()
    #iterate over words
    #while index <= len(words)-1:
    for index in range(len(words)):
        if index <= len(words)-2:
            pair_word1 = words[index]
            pair_word2 = words[index + 1]
    #     #add two words to a tuple
            words_in_tuple = (pair_word1, pair_word2)
            next_word = words[index + 2]
            # check if words_in_tuple in dictionary:
            
            # if it is: update the value: 
                     # append()??
            # else: 
                chains[words_in_tuple] = [next_word]



    #         print words_in_tuple
    #         set_of_tuples.add(words_in_tuple)
            
    # print set_of_tuples

    # #search for tuple(consecutive words) in words
    # if pair_word1 and pair_word2 in words:
    #     next_word = pair_word2 + 1
        #new list

        #append tuple + 1 to new list each time that tuple is found

        #assign tuple as key in dictionary
        #assign all possibilities including duplicates as the value
            #chains[words_in_tuple] = [new list]


        


    return chains

    # for item in lists:

    # for index in _____ lists:


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
