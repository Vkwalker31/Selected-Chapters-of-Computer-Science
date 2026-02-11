# ---------------------------------------------------------
# Lab Work №3 - Task 3 (Variant 9)
# Purpose: In a line entered from the keyboard, count the number of spaces and punctuation marks
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-02-01
# ---------------------------------------------------------

import inputValidator

DESCRIPTION = """In a line entered from the keyboard, 
count the number of spaces and punctuation marks"""

PUNCTUATION_MARKS = '.,;:!?-—…"\'()[]{}«»'


def get_input_string():
    """
    Function to get a string from the user

    Returns:
        String entered by user
    """
    return inputValidator.input_data_with_random("Input string: ", str,
                                                is_generate_random=True,
                                                is_printing_generate_value=True)


def count_spaces_and_punctuation(string_value):
    """
    Function to count spaces and punctuation marks in a string

    Args:
        string_value: Input string

    Returns:
        Tuple of (space_count, punctuation_count)
    """
    space_count = 0
    punctuation_count = 0

    for character in string_value:
        if character == ' ':
            space_count += 1
        elif character in PUNCTUATION_MARKS:
            punctuation_count += 1

    return space_count, punctuation_count


def print_result(space_count, punctuation_count):
    """
    Function to display the result

    Args:
        space_count: Number of spaces
        punctuation_count: Number of punctuation marks
    """
    print(f"Number of spaces: {space_count}")
    print(f"Number of punctuation marks: {punctuation_count}")
    print(f"Total: {space_count + punctuation_count}")


def print_description():
    """Function for describing the task condition"""
    print(DESCRIPTION, end="\n\n")


def task3():
    """The main function to start the whole process"""
    print_description()
    string_value = get_input_string()
    space_count, punctuation_count = count_spaces_and_punctuation(string_value)
    print_result(space_count, punctuation_count)
