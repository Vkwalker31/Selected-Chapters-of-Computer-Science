# ---------------------------------------------------------
# Lab Work №3 - Task 1 (Variant 9)
# Purpose: Calculate arccos(x) using power series expansion
# Formula: arccos(x) = π/2 - arcsin(x) = π/2 - Σ(n=0 to ∞) [(2n)! / (4^n * (n!)^2 * (2n+1))] * x^(2n+1)
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-01-01
# ---------------------------------------------------------

from tabulate import tabulate
import math
import inputValidator

DESCRIPTION = """Write a program to calculate the value of arccos(x)
using its power series expansion: arccos(x) = π/2 - arcsin(x) = π/2 - Σ [(2n)! / (4^n * (n!)^2 * (2n+1))] * x^(2n+1)
where |x| ≤ 1"""

MAX_ITERATION = 500
TITLE_TABLE = ["x", "n", "F(x)", "Math F(x)", "eps"]

def print_description():
    """Function for describing the task condition"""
    print(DESCRIPTION, end= "\n\n")

def print_table(func):
    """
        Decorator function for outputting results in a table

        Args:
            func: Function to wrap

        Returns:
            Wrapper function
        """

    def wrapper_in_table(*args, **kwargs):
        result = func(*args, **kwargs)
        print(tabulate([result], headers=TITLE_TABLE, tablefmt="grid", floatfmt=".10f"))
        return result

    return wrapper_in_table


def get_validate_inputs():
    """
    Function to receive input from the user

    Returns:
        Tuple of (eps, x) values
    """
    eps = inputValidator.input_data_with_random("Input value from 0 to 1 for eps: ",
                                               float, 1e-10, 0.999, is_generate_random=True)
    x = inputValidator.input_data_with_random("Input argument func, where |x| <= 1: ",
                                             float, -1.0, 1.0, is_generate_random=True)

    return eps, x


def factorial(n):
    """
    Calculate factorial of n

    Args:
        n: Integer number

    Returns:
        Factorial of n
    """
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@print_table
def calculate(eps, x):
    """
    Function for calculating arccos(x) using series until a specified accuracy is reached

    Args:
        eps: Desired accuracy
        x: Argument value

    Returns:
        Tuple of (x, iterations, calculated_value, math_value, eps)
    """
    math_fx = math.acos(x)  # Reference value using math library

    # arccos(x) = π/2 - arcsin(x)
    # arcsin(x) = Σ(n=0 to ∞) [(2n)! / (4^n * (n!)^2 * (2n+1))] * x^(2n+1)

    arcsin_sum = 0
    n = 0

    while n < MAX_ITERATION:
        # Calculate term: [(2n)! / (4^n * (n!)^2 * (2n+1))] * x^(2n+1)
        numerator = factorial(2 * n)
        denominator = (4 ** n) * (factorial(n) ** 2) * (2 * n + 1)
        term = (numerator / denominator) * (x ** (2 * n + 1))

        arcsin_sum += term

        # Check convergence
        if abs(term) < eps:
            break

        n += 1

    fx = (math.pi / 2) - arcsin_sum  # arccos(x) = π/2 - arcsin(x)

    return x, n + 1, fx, math_fx, eps


def task1():
    """The main function to start the whole process"""
    print_description()
    eps, x = get_validate_inputs()
    calculate(eps, x)