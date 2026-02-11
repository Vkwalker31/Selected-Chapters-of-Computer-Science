# ---------------------------------------------------------
# Lab Work №3 - Task 2 (Variant 9)
# Purpose: Create a loop that takes integers and calculates the average of even numbers
# The loop ends when the number 0 is entered
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-01-01
# ---------------------------------------------------------

import inputValidator

DESCRIPTION = """Create a loop that takes integers and calculates 
the average of even numbers. The loop ends when the number 0 is entered"""


def get_numbers():
    """
    Function to get numbers from user

    Returns:
        List of entered numbers
    """
    list_numbers = []

    while True:
        num = inputValidator.input_data_with_random("Input integer num or 0 for finishing input: ", int,
                                                   is_generate_random=True, is_printing_generate_value=True)
        if num != 0:
            list_numbers.append(num)
        else:
            break

    return list_numbers


def calculate_average_even(numbers):
    """
    Function to calculate average of even numbers

    Args:
        numbers: List of integers

    Returns:
        Average value of even numbers or None if no even numbers
    """
    even_numbers = [num for num in numbers if num % 2 == 0]

    if even_numbers:
        return sum(even_numbers) / len(even_numbers)
    else:
        return None


def print_result(average):
    """
    Function to display the result

    Args:
        average: Average value to display
    """
    if average is not None:
        print(f"The average of even numbers is: {average}")
    else:
        print("No even numbers were entered")


def print_description():
    """Function for describing the task condition"""
    print(DESCRIPTION, end="\n\n")


def task2():
    """The main function to start the whole process"""
    print_description()
    numbers = get_numbers()
    average = calculate_average_even(numbers)
    print_result(average)
