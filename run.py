

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2)
    return number_1 - number_2

def multiply(number_1, number_2)
    return number_1 * number_2

def divide(number_1, number_2)
    return number_1 / number_2

def numbers():
    try:
        number_1 = int(input("Enter a number: ")) 
    except ValueError:
        print("You have not entered a number. Please enter a number.") 
    try:   
        number_2 = int(input("Enter another number: "))
    except ValueError: 
        print("You have not entered a number. Please enter a number.")

def calculation():

    operator = input("Choose an operator from the following + - * /: ")

    if operator == "+":
        result = number_1 + number_2
        print(number_1, "+", number_2, "=", result)
    elif operator == "-":
        result = number_1 - number_2
        print(number_1, "-", number_2, "=", result)
    elif operator == "*":
        result = number_1 * number_2
        print(number_1, "*", number_2, "=", result)
    elif operator == "/":
        result = number_1 / number_2
        print(number_1, "/", number_2, "=", result)
    else:
        print("You have not entered a valid operator, please try again.")
        calculation()


    another_calculation()


def another_calculation():
    new_calculation = input("Do you want to do another calculation? y / n ")
    if new_calculation.lower() == "y":
        calculation()
    elif new_calculation.lower() == "n":
        print("Bye for now!")
    else:
        print("Invalid input. Please enter y or n")
        another_calculation()


calculation()

