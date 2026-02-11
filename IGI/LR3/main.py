# ---------------------------------------------------------
# Lab Work №3
# Topic: Standard Data Types, Collections, Functions, Modules
# Goal: Master the basic syntax of Python, gain skills working with standard data types,
# collections, functions, modules, and reinforce them by developing interactive applications.
# Version: 1.0
# Developer: Vodnev Kirill
# Date of Development: 2026-02-01
# ---------------------------------------------------------

import inputValidator
import task1
import task2
import task3
import task4
import task5


def run_task1():
    """Execute Task 1"""
    task1.task1()

def run_task2():
    """Execute Task 2"""
    task2.task2()

def run_task3():
    """Execute Task 3"""
    task3.task3()

def run_task4():
    """Execute Task 4"""
    task4.task4()

def run_task5():
    """Execute Task 5"""
    task5.task5()

def main() -> None:
    """Main function to run the program"""
    while True:
        print("\n" + "=" * 50)
        print("Laboratory Work №3 - Menu")
        print("=" * 50)
        print("1. Task 1: Calculate arccos(x) using series")
        print("2. Task 2: Average of even numbers")
        print("3. Task 3: Count spaces and punctuation")
        print("4. Task 4: Text analysis")
        print("5. Task 5: Process real number list")
        print("0. Exit")
        print("=" * 50)

        select = inputValidator.input_data("Input number of task: ", int, 0, 5)

        match select:
            case 1:
                run_task1()
            case 2:
                run_task2()
            case 3:
                run_task3()
            case 4:
                run_task4()
            case 5:
                run_task5()
            case 0:
                print("Exiting program. Goodbye!")
                break

if __name__ == "__main__":
    main()
