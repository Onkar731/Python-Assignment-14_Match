"""
Write a python script to check whether a given number is positive, negative or zero
"""

# taking input from the user
num = int(input("Enter a number : "))

# checking whether the given number is positive, negative or zero
# conditional casing is used
match num :
    case num if num > 0:
        print("Positive")
    case num if num < 0:
        print("Negative")
    case _:
        print("Zero")

# another logic
"""
    match num > 0:
        case True :
            print("Positive")
        case _ :
            if num < 0 :
                print("Negative")
            else :
                print("Zero")
"""
        