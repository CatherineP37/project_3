
"""
This is a while loop to run code while the user wants to do a calculation.

"""

another_calculation = True

while another_calculation is True:

    """
    These are the calculation functions.

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
    This is the where the user enters the information for the calculation.

    """

    number_1 = int(input("Enter a number: "))

    operator = input("Choose an operator (+, -, *, /) ")

    number_2 = int(input("Enter another number: "))  

    """
    This is an if statement for the different operators

    """

    if operator == "+":
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif operator == "-":
        print(number_1, "-", number_2, "=", subtract(number_1, number_2)) 
    elif operator == "*":
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif operator == "/":
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    else:
        print("Please enter +, -, * or /")
    
    """
    This if statement closes the calculator is the user enters 'no'.

    """

    new_calculation = input("Do you want to do another calculation? (yes/no) ")
    if new_calculation == 'no':
        another_calculation = False
