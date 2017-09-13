# String: TCTAGGGGGGATCCCCCTAGATCTAGGGGGATCCCCCCTAGA
import math


def get_substrings(string):
    for start_index in range(len(string)):
        for end_index in range(len(string), start_index, -1):
            yield string[start_index:end_index]


def is_palindrome(string):
    if string[0:(len(string)//2) - 1] == string[len(string):math.ceil(len(string)/2):-1]:
        return True
    return False


def longest_palindrome(string):
    longest = ""
    for substring in get_substrings(string):
        # print("checking substring", substring, "...", is_palindrome(substring))
        if is_palindrome(substring) and len(substring) > len(longest):
            longest = substring
    return longest


if __name__ == '__main__':
    _input = input('String to search?\n')
    winner = longest_palindrome(_input)
    print(winner, len(winner))
    input()
