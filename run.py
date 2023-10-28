# memory functionality adapted from stackoverflow.com/questions/29091791/python-calculator-with-memory-function

calculations = []
def record_history(num1, num2):
    record = f"{num1} + {num2} = {num1 + num2}"
    calculations.append(record)

def history():
    if calculations == []:
        print("No past calculations to show")
    elif conditon:
        print(calculations[-1])
        print(calculations[-2])
        print(calculations[-3])
    else:
        for i in calculations:
            print(i)

def add(n1, n2):
    record_history(n1 , n2)
    return n1 + n2

def subtract(n1, n2):
    record_history(n1 , n2) 
    return n1 - n2

def multiply(n1, n2):
    record_history(n1 , n2)
    return n1 * n2

def divide(n1, n2):
    record_history(n1 , n2)
    return n1 / n2

def number_one():
    print(
         #####                                                                
#     #   ##   #       ####  #    # #        ##   #####  ####  #####  
#        #  #  #      #    # #    # #       #  #    #   #    # #    # 
#       #    # #      #      #    # #      #    #   #   #    # #    # 
#       ###### #      #      #    # #      ######   #   #    # #####  
#     # #    # #      #    # #    # #      #    #   #   #    # #   #  
 #####  #    # ######  ####   ####  ###### #    #   #    ####  #    # 
                                                                      
     )
    while True:
        try:
            global number_1
            number_1 = int(input("Enter a number:\n")) 
            number_two()
        except ValueError:
            print("You have not entered a number. Please enter a number.")

def number_two():
    while True:
        try:  
            global number_2 
            number_2 = int(input("Enter another number:\n"))
            calculation()
        except ValueError: 
            print("You have not entered a number. Please enter a number.")

def calculation():

    operator = input("Choose an operator from the following + - * /:\n")

    if operator == "+":        
        print(number_1, "+", number_2, "=", add(number_1, number_2))
        print(calculations)
    elif operator == "-":     
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    elif operator == "*":        
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif operator == "/":  
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    else:
        print("You have not entered a valid operator, please try again.")
        calculation()

    another_calculation()


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
