# Author: Leonel Garay
# Date: 11/11/2019
# Description: Takes wo strings as parameters and returns a set of the words contained in both strings.


def words_in_both(string_1, string_2):
    """Takes wo strings as parameters and returns a set of the words contained in both strings."""
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    string_1 = string_1.split()  # Splits string_1 into words
    string_2 = string_2.split()  # Splits string_2 into words
    word_set = set()  # Blank set
    for character in string_1:  # Looks at each word in string_1 and compares it to words in string_2
        if character in string_2:
            word_set.add(character)  # If word is found on word_2 add it to the empty set (word_set)
    return word_set
