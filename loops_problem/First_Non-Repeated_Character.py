# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

sentense = "this is the python programming problem"

for char in sentense:
    if sentense.count(char) == 1:
        print(char)
        break

