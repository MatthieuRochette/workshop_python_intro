#!/usr/bin/env python3
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex06
##
import sys

def ex06(av):
    arg = -1
    num = 0
    for v in av:
        if arg != -1:
            for letter in v:
                if num == 0:
                    print(letter, end = '')
                num += 1
            num = 0
        arg += 1
    print()

if __name__ == "__main__":
    ex06(sys.argv)