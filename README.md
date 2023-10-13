![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Simple Calculator

This is a simple calculator that does addition, subtraction, multiplication and division.

## Features

### First number input

### Operator input

### Second number input

### Calculation and result

### Option to do another calculation

## Testing

I tested the code with Pyton Syntax Checker PEP8 and had no major issues with it. It flagged up some issues with not puting white space around operators and other similar issues. I fixed most of these issues.

## Bugs

There was an indentation problem but it was resolved.

There was also a problem with syntax. That was resolved by replacing a = with ==.

The calculation part of the project is not working. It's showing the word "none" instead of the result of the calculation. This was resolved by adding the word "return" to the functions.

The calculator doesn't close when the user replies "no" to the question about whether they want to do another calculation. This problem has been resolved.

If the user entered an invalid operator, the game asked for them to enter another number instead of giving the error message straight away. The error message came after the user entered the second number. This issue was resolved by moving the input statement for the second number so that it comes before the operator input statement. 

There is another issue with the error handling. Straight after the error message is given, the user is asked if they want to do another calculation.

## Deployment

## Credits

I took inspiration from the following projects:

[Programiz](https://www.programiz.com/python-programming/examples/calculator)

[Built in](https://builtin.com/software-engineering-perspectives/python-calculator)