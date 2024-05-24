
# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

'''
num = 5

factorial = num;
if (num == 1 or num == 0):
    factorial = 1
else:
    while num > 1:
        factorial *= num -1
        num -=1

print(factorial)

'''

# 2nd method (chai):

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
print("factorial = ",factorial)