def calculation():
    number_1 = int(input("Enter a number: "))
	operator = input("Choose an operator from the following: + - * / ")
	number_2 = int(input("Enter another number: "))

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

def another_calculation():
	new_calculation = input("Do you want to do another calculation? yes/no ")
	if new_calculation == "yes":
	    calculation()
	elif new_calculation == "no":
		print("Thanks for the calculation.")
	else:
		another_calculation()
        
calculation()


