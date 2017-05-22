import sys, time
sys.path.append('C:\\Users\\nxtfa\\Desktop\\Programming\\my lib')
from testsuite import *

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

def find_unknown_words(vocab, wds):
    '''return a list of words in wds that do not occur in vocab'''
    result = []
    for w in wds:
        if search_binary(vocab, w) == -1:
            result.append(w)
    return result

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

def text_to_words(the_text):
    """return a list of words with all punctuation removed, and all in lowercase."""

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

def search_binary(xs, target, verbose=False):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]
        if verbose:
            print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
               .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

if __name__ == "__main__":
    # Linear algorithm test suite
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    test(search_linear(friends, "Zoe") == 1)
    test(search_linear(friends, "Joe") == 0)
    test(search_linear(friends, "Paris") == 6)
    test(search_linear(friends, "Bill") == -1)

    # Find unknown words in list test suite
    vocab = ["apple", "boy", "dog", "down",
                              "fell", "girl", "grass", "the", "tree"]
    book_words = "the apple fell from the tree to the grass".split()
    test(find_unknown_words(vocab, book_words) == ["from", "to"])
    test(find_unknown_words([], book_words) == book_words)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])

    # Text to words test suite
    test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
    test(text_to_words('"Well, I never!", said Alice.') ==
                                 ["well", "i", "never", "said", "alice"])

    # Binary algorithm test suite
    xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
    test(search_binary(xs, 20) == -1)
    test(search_binary(xs, 99) == -1)
    test(search_binary(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        test(search_binary(xs, v) == i)
    input()
