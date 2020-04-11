##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex03
##

from sys import argv as av

def ex03():
    for arg in av[1:]: # for each argument (excepted the first)
        for i in arg: # for each letter in the argument
            if i == "z" or i == "Z":
                print(chr(ord(i) - 25), end="")
            elif i.isalpha():
                print(chr(ord(i) + 1), end="")
            else:
                print(i, end="")
        print()

if __name__ == "__main__":
    try:
        ex03()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")