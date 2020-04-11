#!/usr/bin/env python3
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex05
##

from sys import argv as av

def ex05():
    for arg in av[1:]:
        for i in arg:
            if i == "z" or i == "Z":
                print(chr(ord(i) - 25), end="")
            elif i.isalpha():
                print(chr(ord(i) + 1), end="")
            else:
                print(i, end="")
        print()

if __name__ == "__main__":
    try:
        ex05()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")