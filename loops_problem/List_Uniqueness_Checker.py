# List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]


# Approach 1
'''
items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) > 1:
        print(item,"is duplicate") 
        break

'''

# Approach 2:

items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate",item)
    unique_items.add(item)

