##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex02
##

from sys import argv as av #import only argv, aliased as av

def print_cli_args():
    print(*av, sep=" ") # sep -> string to write between each argument of print (default = ' ')
    # other setting of print(): end -> string to write after the last argument (default = '\n')
    # putting '*' before a list unfolds it ([1, 2, 3] -> 1, 2, 3)

if __name__ == "__main__":
    try:
        print_cli_args()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")