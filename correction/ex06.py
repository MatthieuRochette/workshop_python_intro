##
## EPITECH PROJECT, 2020
## workshop_python_intro
## File description:
## ex06
##

def ex06():
    vowel_count = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
        "y": 0,
        "Total": 0
    }

    #This is a good way to open a file.
    with open("test.txt", "r") as file:
        #for each line of a file...
        for line in file.readlines():
            if "42" in line:
                print(line, end="")
            #for each character of a line...
            for i in line:
                try:
                    vowel_count[i] += 1
                except KeyError:
                    pass
                except Exception:
                    exit(84)
    print()
    for item in vowel_count.items():
        if item[0] != "Total":
            vowel_count["Total"] += item[1]
    for key, value in vowel_count.items():
        print("{}: {}".format(key, value))

if __name__ == "__main__":
    try:
        ex06()
    except Exception as excp:
        print("Your program encountered an error.")
        print("Error:", excp)
        exit(84)
    print("Congratulations ! You finished this exercise.")