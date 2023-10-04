# Author: Leonel Garay
# Date: 11/09/2019
# Description: Takes as a parameter a string and returns a dictionary with a letter count, excludes non-letters.


def count_letters(word):
    """Takes as a parameter a string and returns a dictionary with a letter count."""
    word = word.upper()  # All characters in dictionary should be capitalized.
    letter_dic = {}  # Dictionary with characters.
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"  # List of all character that cna be added to dictionary.
    for character in word:
        if character in alphabet:  # Looks for any letter that is in the alphabet string.
            if character not in letter_dic:  # If character is already in dictionary add 1, if not equal 1.
                letter_dic[character] = 1
            else:
                letter_dic[character] += 1
    return letter_dic
