##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex01
##

def my_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError: # return 0 if python raises ZeroDivisionError
        return 0

if __name__ == "__main__":
    try:
        calcs = {
            (52, 13): "4.000",
            (4, 98): "0.041",
            (-7, 64): "-0.109",
            (-84, -13): "6.462",
            (0, 15): "0.000",
            (15, 0): "0.000"
        }
        for pair, answer in calcs.items():
            result = "{0:.3f}".format(my_divide(*pair))
            if result != answer:
                raise Exception("bruh")
            print("{0} / {1} = {2}".format(pair, pair, result))
    except Exception as excp:
        print("The program ran into an error at this pair of numbers: {}".format(pair))
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")