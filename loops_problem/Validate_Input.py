# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

num = 0
while (num < 1 or num > 10):
    num = int(input("Enter number : "))
    print("Invalid input,Try again")
print("THaks")

