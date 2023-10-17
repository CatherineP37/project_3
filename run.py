def calculation():
    number_1 = int(input("Enter a number: "))
	operator = int(input("Choose an operator from the following: + - * / "))
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


