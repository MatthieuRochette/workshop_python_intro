##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex05
##

"""
------------------------------- TO DO ------------------------------------------
Write a program which does the following things:
    - Ask the user for a number.
    - Ask the user for a second number.
    - Ask the user for an operation. ('+', '-', '*', '/', '%')
    - Finally, display the whole calculation.

You should implement some error handling in your program. (division by zero,
invalid parameter, etc...)

You should try to make your code the cleanest possible. (reusable functions, no
useless variables, separate your code in multiple functions)

You must raise execeptions in your program with the following messages:
    - "Invalid number(s)."
    - "Invalid operator."
    - "Division by zero."
    - "Modulo by zero."

#Hint: input(), raise Exception()

#Exemple 1: Valid arguments

number a:10
number b:20
operation:+
10 + 20 = 30

#Exemple 2: Invalid number

number a:a
Invalid number(s).

#Exemple 3: Invalid operator

number a:10
number b:20
operation:toto
Invalid operator.

#Exemple 4: Division by zero

number a:10
number b:0
operation:/
Division by zero.

--------------------------------------------------------------------------------
"""

def my_calcul():
    #Write your program hereunder

if __name__ == "__main__":
    try:
        my_calcul()
    except Exception as e:
        print(e)