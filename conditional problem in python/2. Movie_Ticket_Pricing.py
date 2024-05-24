# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


# Method 1
'''
age = int(input("Enter your age: "))
day = input("Enter movie day: ")

if age >= 18:
    if day.lower() == "wednesday":
        print("Your Ticket price is $10 after $2 discount")
    else:
        print("Your Ticket price is $12")
else:
    if day.lower() == "wednesday":
        print("Your Ticket price is $6 after $2 discount")
    else:
        print("Your Ticket price is $8")

'''


# 2nd method:
age = 20
day = "wednesday"

price = 12 if age > 18 else 8

if day == "wednesday":
    price -= 2

print("your tickek price is : $",price)