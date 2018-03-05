"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    our_file = open(file_path)
    return our_file.read()


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
    """
    chains = {}

    words = text_string.split()  # Put str into liist

    #iterate over words
    for index in range(len(words)):
        if index <= len(words)-3:  # Make sure there is enough words to create values
            
            # get the words for bi-gram
            pair_word1 = words[index]
            pair_word2 = words[index + 1]
            
            # add two words to a tuple
            words_in_tuple = (pair_word1, pair_word2)
            
            next_word = words[index + 2]
            # check if words_in_tuple in dictionary:
            if words_in_tuple in chains:
            # if it is: update the value
                chains[words_in_tuple].append(next_word)
            # if not create new key-value pair
            else:
                chains[words_in_tuple] = [next_word]
    return chains


def make_text(chains):
    """Return text from chains."""

    our_words = []

    # Make a link (tuple --> random word in connected words list)
    # Get the initial state (beginning bi-gram)
    bigrams = chains.keys()  # List of all possible bi-grmas from text
    current_pair = choice(bigrams)  # Choose random bi-gram to start
    our_words.extend(current_pair)  # Add to list

    # Continue to make links until reach end of text
    while chains.get(current_pair) is not None:  # While there is still a tuple to get
        link_list = chains[current_pair]  # List of words linked to current bi-gram
        
        # Choose word from list of linked words
        chosen_word = choice(link_list)
        
        # Add words to list to create semi-random text
        our_words.append(chosen_word)

        # Make a new key
        new_pair = (current_pair[1], chosen_word)
        current_pair = new_pair

        # ..... Repeat

    return " ".join(our_words)

input_path = sys.argv[1]
#input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
