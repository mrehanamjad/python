# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

try:
    age = int(input("Enter your age: "))
    
    if age > 0 and age < 13:
        print("You are a child")
    elif age < 19:
        print("You are a teenager")
    elif age < 59:
        print("You are an adult")
    else:
        print("You are a senior")
except :
    print("Invalid input: Please enter a valid number")

""" 
if use input a character or string it shows error to handel that error
we has used :
    try: 
        ...
    except ValueError:
        ...  


"""  