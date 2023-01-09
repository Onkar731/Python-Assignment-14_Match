"""
Write a python script to make a menu driven program in which user has to choose one
of the option from four given options -
1) Odd-Even 2) Positive - Non_positive 3) Simple Interest 4) Find roots of quadratic equation
Match and execute appropriate code on user selection
"""

# displaying menu for the user
print("1. Odd-Even", "2. Positive - Non positive", "3. Simple Interest", "4. Find roots of quadratic equation", sep="\n")

# taking choice of the user
choice = int(input("Enter your choice : "))

# defining match block
match choice :
    case 1 :
        num = int(input("Enter a number : "))
        
        # evaluating whether it is even or odd
        if num%2 == 0 :
            print("Even")
        else :
            print("Odd")
    case 2 :
        num = int(input("Enter a number : "))
        
        # evaluating whether it is positive, negative or zero
        if num > 0 :
            print("Positive")
        elif num < 0 :
            print("Negative")
        else :
            print("Zero")
    case 3 :
        p_amt, roi, time = float(input("Enter principle amount, rate of interest and time : ")), float(input()), float(input())
        
        # calculating simple interest 
        print("Simple Interest is", (p_amt*roi*time)//100)
    case 4 :
        a, b, c = int(input("Enter values of quadratic euqation : ")), int(input()), int(input())
        
        # calculating discriminant 
        discriminant = b*b - 4*a*c
        
        # checking roots
        if discriminant > 0 :
            print("Roots are real and distinct")
        elif discriminant < 0 :
            print("Roots are imaginary")
        else :
            print("Roots are real and euqal")
    case _ :
        print("Invalid choice")
