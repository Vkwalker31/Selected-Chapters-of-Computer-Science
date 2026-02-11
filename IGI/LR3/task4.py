# ---------------------------------------------------------
# Lab Work №3 - Task 4 (Variant 9)
# Purpose: Text analysis without regular expressions
# a) Determine the number of words starting or ending with a vowel
# b) Determine how many times each character is repeated
# c) Display words after commas in alphabetical order
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-02-01
# ---------------------------------------------------------

DESCRIPTION = """a) Determine the number of words starting or ending with a vowel
b) Determine how many times each character is repeated
c) Display words after commas in alphabetical order"""

CONST_STRING = (
    "So she was considering in her own mind, as well as she could, "
    "for the hot day made her feel very sleepy and stupid, "
    "whether the pleasure of making a daisy-chain "
    "would be worth the trouble of getting up "
    "and picking the daisies, "
    "when suddenly a White Rabbit with pink eyes ran close by her."
)

VOWELS = "aeiouAEIOU"


def extract_words(text):
    """
    Extract words from text, removing punctuation

    Args:
        text: Input text

    Returns:
        List of words
    """
    # Remove punctuation and split into words
    cleaned_text = text.replace(',', ' ').replace('.', ' ').replace('-', ' ')
    words = cleaned_text.split()
    return words


def count_vowel_words(words):
    """
    Function to count words starting or ending with a vowel

    Args:
        words: List of words

    Returns:
        Count of words starting or ending with vowel
    """
    count = 0

    for word in words:
        if word:  # Check if word is not empty
            if word[0] in VOWELS or word[-1] in VOWELS:
                count += 1

    return count


def count_character_repeatability(text):
    """
    Function to count the frequency of each character in the text

    Args:
        text: Input text

    Returns:
        Dictionary with character frequencies
    """
    char_dict = {}

    for character in text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    return char_dict


def get_words_after_commas(text):
    """
    Function to extract and sort words that come after commas

    Args:
        text: Input text

    Returns:
        Sorted list of words after commas
    """
    # Split by commas
    parts = text.split(',')
    words_after_commas = []

    # For each part after comma (skip first part before first comma)
    for i in range(1, len(parts)):
        part = parts[i].strip()
        # Extract first word after comma
        words = part.replace('.', '').split()
        if words:
            words_after_commas.append(words[0].lower())

    # Sort alphabetically
    return sorted(words_after_commas)

def print_description():
    """Function for describing the task condition"""
    print(DESCRIPTION, end="\n\n")

def task4():
    """The main function to start the whole process"""
    print_description()

    print(f"Text: {CONST_STRING}\n")

    # ---------------------------------- a --------------------------------------------------------
    words = extract_words(CONST_STRING)
    vowel_word_count = count_vowel_words(words)
    print(f"a) Number of words starting or ending with a vowel: {vowel_word_count}\n")
    # ---------------------------------- b --------------------------------------------------------
    char_dict = count_character_repeatability(CONST_STRING)
    print("b) Character repeatability:")
    for char, count in sorted(char_dict.items()):
        print(f"   '{char}': {count}")
    print()
    # ---------------------------------- c --------------------------------------------------------
    words_after_commas = get_words_after_commas(CONST_STRING)
    print(f"c) Words after commas in alphabetical order: {words_after_commas}")
