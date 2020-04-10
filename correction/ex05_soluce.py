#!/usr/bin/env python3
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex05
##
import sys

def ex05(av):
    arg = -1
    for v in av:
        if arg != -1:
            for letter in v:
                letter_val = ord(letter) + 1
                print(chr(letter_val), end = '')
        print(" ", end = '')
        arg += 1
    print()

if __name__ == "__main__":
    ex05(sys.argv)
