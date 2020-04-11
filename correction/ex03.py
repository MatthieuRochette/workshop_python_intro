##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex03
##

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise Exception("Division by zero.")
    return a / b

def modulo(a, b):
    if b == 0:
        raise Exception("Modulo by zero.")
    return a % b

def my_calcul():
    #Setup a dictionary with operations as keys and a function as values.
    available_operation = {
        "+": addition,
        "-": substraction,
        "*": multiplication,
        "/": division,
        "%": modulo
    }
    #We cast the return value of input as an int, if there is an error during the cast, it's an invalid parameter.
    try:
        nb_a = int(input("number a:"))
        nb_b = int(input("number b:"))
    except:
        raise Exception("Invalid number(s).")
    operation = input("operation:")
    if operation not in available_operation:
        raise Exception("Invalid operator.")
    print("{} {} {} = {}".format(nb_a, operation, nb_b, available_operation[operation](nb_a, nb_b)))

if __name__ == "__main__":
    try:
        my_calcul()
    except Exception as e:
        print(e)