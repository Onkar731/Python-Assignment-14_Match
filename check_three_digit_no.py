"""
Write a python script to check whether a given number is a three digit number or not
"""

# taking input from the user
num = int(input("Enter a three digit number : "))

# evaluating whether it is a three digit number or not    
match num :
    case num if num >= 100 and num <= 999 or num <= -100 and num >= -999 :
        print(num, "is a three digit number")
    case _ :
        print(num, "is not a three digit number")
        