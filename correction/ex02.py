##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex02
##

from sys import argv as av

def print_cli_args():
    print(*av, sep=" ")

if __name__ == "__main__":
    try:
        print_cli_args()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")