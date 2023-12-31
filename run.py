print("""
 #####
#     #   ##   #       ####  #    # #        ##   #####  ####  #####
#        #  #  #      #    # #    # #       #  #    #   #    # #    #
#       #    # #      #      #    # #      #    #   #   #    # #    #
#       ###### #      #      #    # #      ######   #   #    # #####
#     # #    # #      #    # #    # #      #    #   #   #    # #   #
 #####  #    # ######  ####   ####  ###### #    #   #    ####  #    #
""")
"""
Functions for addition, subtraction, multiplication and division.

"""

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

"""
Input for the first number of the calculation.

"""

def number_one():
    try:
        global number_1
        number_1 = int(input("Enter a number:\n"))
        number_two()
    except ValueError:
        print("You have not entered a number. Please enter a number.")
        number_one()

"""
Input for the second number of the calculation.

"""

def number_two():
    try:
        global number_2
        number_2 = int(input("Enter another number:\n"))
        calculation()
    except ValueError:
        print("You have not entered a number. Please enter a number.")
        number_two()

"""
Function that deals with the operator input and the printing of the calculation and result.

"""

def calculation():

    operator = input("Choose an operator from the following + - * /:\n")

    if operator == "+":
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif operator == "-":
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    elif operator == "*":
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif operator == "/":
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    else:
        print("You have not entered a valid operator, please try again.")

    another_calculation()

"""
Function that asks the user if they want to do another calculation.

"""
def another_calculation():
    new_calculation = input("Do you want to do another calculation? y / n\n")
    if new_calculation.lower() == "y":
        number_one()
    elif new_calculation.lower() == "n":
        print("Bye for now!")
    else:
        print("Invalid input. Please enter y or n")
        another_calculation()


number_one()