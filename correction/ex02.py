##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex01
##

"""
------------------------------- TO DO ------------------------------------------
Write a program that print the arguments given in the command line, separated by a space, including the name of the Python file.
It shall print a new line when all the arguments have been printed.

!!! There should not be spaces before the first of after the last arguments !!!

Hint: import sys

Bonus : Try to do it in only one line of code !
--------------------------------------------------------------------------------
"""

#Do your imports hereunder
from sys import argv as av

def print_cli_args():
    #Write your program hereunder
    print(av, sep=" ")


#Tests
if __name__ == "__main__":
    try:
        print_cli_args()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")