##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex00b
##

"""
------------------------------- TO DO ------------------------------------------
Swap a and b without a third variable.

Hint: You can declare multiple variables on the same line !
--------------------------------------------------------------------------------
"""

def my_swap(a, b):
    #Write your code here
    

    #Don't worry about that
    return (a, b)


if __name__ == "__main__":
    v1s = [5, 45, 2, 0, "aerd", 0.34]
    v2s = [6, 'bhkl', 524, 0.2, 45, 2]
    try:
        for i in range(len(v1s)):
            v1, v2 = v1s[i], v2s[i]
            print("Before swap: ", end="")
            print("a={}, b={}".format(v1, v2))
            v1, v2 = my_swap(v1, v2)
            print("After swap: ", end="")
            print("a={}, b={}".format(v1, v2))
            if i < len(v1s):
                print()
    except Exception as excp:
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")