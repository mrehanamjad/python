# 8. Prime Number Checker
# Problem: Check if a number is prime.

# Approach 1
'''
num = int(input("Enter a number-2 : "))
factor_count = 0


for i in range(1,num+1):
    if num % i == 0:
        factor_count+=1

if factor_count == 2:
    print(num,"is prime number")
else:
    print(num,"is NOT a prime number")

'''

# Approach 2

num = int(input("Enter a number : "))
is_prime = True

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            is_prime = False
            break

if is_prime:
    print(num,"is prime number")
else:
    print(num,"is NOT a prime number")