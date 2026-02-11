# ---------------------------------------------------------
# Lab Work №3
# Module: generateRandom
# Purpose: Module for generating random values
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-01-01
# ---------------------------------------------------------

import random
import string

def print_generate_number(generate_value):
    """Function for outputting result generate value"""
    print("\nGenerated value:", generate_value, "\n")

def generate_random(data_type, min_value=None, max_value=None, is_printing_generate_value=False):
    """
    Function to generate random data based on the specified data type and optional value range constraints

    Args:
        data_type: Type of data to generate (int, float, str)
        min_value: Minimum value for generation
        max_value: Maximum value for generation
        is_printing_generate_value: Flag to print generated value

    Returns:
        Generated random value of specified type
    """
    if data_type == str:
        if min_value is None:
            min_value = 1
        if max_value is None:
            max_value = 10

        generated_value = ''.join(
            random.choices(string.ascii_letters + string.digits + string.punctuation + ' ',
                           k=random.randint(min_value, max_value)))

        if is_printing_generate_value:
            print_generate_number(generated_value)

        return generated_value

    if min_value is None and data_type == float:
        min_value = -1e307
    elif min_value is None and data_type == int:
        min_value = -2_147_483_648

    if max_value is None and data_type == float:
        max_value = 1e307
    elif max_value is None and data_type == int:
        max_value = 2_147_483_647

    if data_type == int:
        generated_value = random.randint(min_value, max_value)
    elif data_type == float:
        generated_value = random.uniform(min_value, max_value)
    else:
        raise ValueError("Unsupported data type. Supported types are int, float, and str.")

    if is_printing_generate_value:
        print_generate_number(generated_value)
    return generated_value

def generate_sequence(data_type, min_value=None, max_value=None, count=None, is_printing_generate_value=False):
    """
    Generator function that yields a sequence of random values

    Args:
        data_type: Type of data to generate
        min_value: Minimum value for generation
        max_value: Maximum value for generation
        count: Number of values to generate
        is_printing_generate_value: Flag to print generated values

    Yields:
        Random values of specified type
    """
    if count is None:
        count = random.randint(10, 100)

    for _ in range(count):
        yield generate_random(data_type, min_value, max_value, is_printing_generate_value=is_printing_generate_value)
