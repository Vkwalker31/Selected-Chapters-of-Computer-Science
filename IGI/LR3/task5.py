# ---------------------------------------------------------
# Lab Work №3 - Task 5 (Variant 9)
# Purpose: Process list of real numbers
# a) Find the product of negative elements
# b) Find the sum of positive elements located before the maximum element
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-02-01
# ---------------------------------------------------------

import inputValidator
import randomGenerator

DESCRIPTION = """a) Find the product of negative elements of the list
b) Find the sum of positive elements located before the maximum element"""


def get_numbers():
    """
    Function to get numbers from user

    Returns:
        List of real numbers
    """
    list_numbers = []
    mode = inputValidator.input_data(description="1 - Generate sequence nums\n0 - Manual input\n",
                                    data_type=int, min_value=0, max_value=1)

    if mode == 1:
        count = inputValidator.input_data("Input count of elements: ", int, min_value=1, max_value=100)
        list_numbers = list(randomGenerator.generate_sequence(data_type=float, min_value=-100, max_value=100,
                                                             count=count, is_printing_generate_value=False))
        print(f"\nGenerated list: {list_numbers}\n")
    else:
        while True:
            num = inputValidator.input_data_with_random("Input float num or 0 for finishing input: ", float,
                                                       is_generate_random=True, is_printing_generate_value=True)
            if num != 0:
                list_numbers.append(num)
            else:
                if not list_numbers:
                    print("List is empty, please enter at least one number")
                    continue
                break

    return list_numbers


def find_max_index(numbers):
    """
    Function to find the index of maximum element

    Args:
        numbers: List of numbers

    Returns:
        Index of maximum element
    """
    max_value = max(numbers)
    return numbers.index(max_value)


def calculate_product_negative(numbers):
    """
    Function to calculate the product of negative elements

    Args:
        numbers: List of numbers

    Returns:
        Product of negative elements or None if no negative elements
    """
    product = 1
    has_negative = False

    for num in numbers:
        if num < 0:
            product *= num
            has_negative = True

    return product if has_negative else None


def calculate_sum_positive_before_max(numbers, max_index):
    """
    Function to calculate the sum of positive elements before maximum element

    Args:
        numbers: List of numbers
        max_index: Index of maximum element

    Returns:
        Sum of positive elements before max or None if no such elements
    """
    sum_positive = 0
    has_positive = False

    for i in range(max_index):
        if numbers[i] > 0:
            sum_positive += numbers[i]
            has_positive = True

    return sum_positive if has_positive else None


def print_description():
    """Function for describing the task condition"""
    print(DESCRIPTION, end="\n\n")


def task5():
    """The main function to start the whole process"""
    print_description()

    list_numbers = get_numbers()

    if list_numbers:
        print(f"List: {list_numbers}\n")

        max_index = find_max_index(list_numbers)
        print(f"Maximum element: {list_numbers[max_index]} (index: {max_index})\n")

        # ---------------------------------- a --------------------------------------------------------
        product_negative = calculate_product_negative(list_numbers)
        if product_negative is not None:
            print(f"a) Product of negative elements: {product_negative}")
        else:
            print("a) No negative elements in the list")

        # ---------------------------------- b --------------------------------------------------------
        sum_positive_before_max = calculate_sum_positive_before_max(list_numbers, max_index)
        if sum_positive_before_max is not None:
            print(f"b) Sum of positive elements before maximum: {sum_positive_before_max}")
        else:
            print("b) No positive elements before maximum element")

    else:
        print("The list is empty")
