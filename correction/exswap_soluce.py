#!/usr/bin/env python3
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## exswap
##

if __name__ == "__main__":
    a = 5
    b = 6
    print("a = " + str (a))
    print("b = " + str (b))
    a, b = b, a
    print("a = " + str (a))
    print("b = " + str (b))