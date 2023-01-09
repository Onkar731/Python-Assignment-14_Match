"""
Write a python script to take one data from user and evaluate the type of data.
If the data is of int type the print Monday, if the data is of float type then print
Tuesday, if the data is of complex type then print Wednesday, if the data is of type
bool then print Thursday.
"""

# taking input from the user
data = eval(input("Enter any type of data : "))

# evaluating type of data
match data :
    case data if type(data) == int :
        print("Monday")
    case data if type(data) == float :
        print("Tuesday")
    case data if type(data) == complex :
        print("Wednesday")
    case data if type(data) == bool :
        print("Thursday")
    case _ :
        print(data, type(data), "not allowed")
