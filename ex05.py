##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex04
##

"""
------------------------------- TO DO ------------------------------------------
Write a program that:
    - opens a file (test.txt, at the root of the repository),
    - counts the number of vowels in the file (list of vowels: "aeiouy")
    - prints every line containing "42"

Hint: Take a look at the keyword 'with' !

Bonus: count separately each vowel
--------------------------------------------------------------------------------
"""

def ex04():
    #Write your code here

#Test
if __name__ == "__main__":
    try:
        ex04()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")