"""
Write a python script to take a string from the user. If the string is a part of 
"mysirg" then print "One", if the string is a part of "education" then print "Two"
and if the string is a part of "services" then print "Three"
"""

# taking string from the user
string = input("Enter a string : ")

# matching string whether it's a part of "mysirg" string or not
match string :
    case string if string in "mysirg" :
        print("One")
    case string if string in "education" :
        print("Two")
    case string if string in "services" :
        print("Three")
    case _ :
        print(string, "is not present in 'mysirg education services'")
