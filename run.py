def add(n1, n2):
    n1 + n2

def subtract(n1, n2):
    n1 - n2

def multiply(n1, n2):
    n1 * n2

def divide(n1, n2):
    n1 / n2

another_calculation = True

while another_calculation is True:

number_1 = int(input("Enter a number: "))

operator = input("Choose an operator (+, -, *, /) ")

number_2 = int(input("Enter another number: "))

new_calculation = input("Do you want to do another calculation? (yes/no) ")
if new_calculation = "no":
    another_calculation = False
