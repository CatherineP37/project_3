def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def numbers():
    try:
        number_1 = int(input("Enter a number: ")) 
    except ValueError:
        print("You have not entered a number. Please enter a number.") 
    try:   
        number_2 = int(input("Enter another number: "))
        calculation()
    except ValueError: 
        print("You have not entered a number. Please enter a number.")

def calculation():

    operator = input("Choose an operator from the following + - * /: ")

    if operator == "+":        
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif operator == "-":     
        print(number_1, "-", number_2, "=", subract(number_1, number_2))
    elif operator == "*":        
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif operator == "/":  
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    else:
        print("You have not entered a valid operator, please try again.")
        calculation()


    another_calculation()


def another_calculation():
    new_calculation = input("Do you want to do another calculation? y / n ")
    if new_calculation.lower() == "y":
        numbers()
    elif new_calculation.lower() == "n":
        print("Bye for now!")
    else:
        print("Invalid input. Please enter y or n")
        another_calculation()




