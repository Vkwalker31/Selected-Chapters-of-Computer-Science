# ---------------------------------------------------------
# Lab Work №3
# Module: inputValidator
# Purpose: Module for input validation and data entry
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-01-01
# ---------------------------------------------------------

import randomGenerator

def input_data(description, data_type, min_value=None, max_value=None):
    """
    Prompts the user for input, validates type and value constraints, and returns the valid input

    Args:
        description: Prompt message for user
        data_type: Expected data type
        min_value: Minimum allowed value
        max_value: Maximum allowed value

    Returns:
        Validated user input
    """
    while True:
        try:
            user_input = data_type(input(description))

            if min_value is not None and user_input < min_value:
                raise ValueError(f"The value have to be greater or = then {min_value}")

            if max_value is not None and user_input > max_value:
                raise ValueError(f"The value have to be less or = then {max_value}")

            return user_input

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid value.")


def input_data_with_random(description, data_type, min_value=None, max_value=None,
                           is_generate_random=False, is_printing_generate_value=False):
    """
    Prompts the user for input, validates type and value constraints, and returns the valid input,
    but generate random value, if user enter word 'random' or 'RANDOM'

    Args:
        description: Prompt message for user
        data_type: Expected data type
        min_value: Minimum allowed value
        max_value: Maximum allowed value
        is_generate_random: Flag to enable random generation
        is_printing_generate_value: Flag to print generated values

    Returns:
        Validated user input or random value
    """
    while True:
        try:
            user_input = input(description)

            if is_generate_random and user_input.upper() == "RANDOM":
                random_value = randomGenerator.generate_random(data_type=data_type, min_value=min_value,
                                                              max_value=max_value,
                                                              is_printing_generate_value=is_printing_generate_value)
                return random_value
            else:
                user_input = data_type(user_input)

            if min_value is not None and user_input < min_value:
                raise ValueError(f"The value have to be greater or = then {min_value}")

            if max_value is not None and user_input > max_value:
                raise ValueError(f"The value have to be less or = then {max_value}")

            return user_input

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid value.")
