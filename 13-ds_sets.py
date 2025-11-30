nums = [1, 1, 2, 3, 3, 4]
uniques = set(nums)
# print(nums)
# print(uniques)

first = {1, 2, 3}
second = {2, 3, 4}

print(3 in first)  # True

print(f"first: {first}")
print(f"second: {second}")
print(f"Union: {first | second}")
print(f"Intersection: {first & second}")
print(f"Substraction: {first - second}")
print(f"Symmetric Difference: {first ^ second}")  # removes common elements

# List comprehension for Sets

sqr_set = {x ** 2 for x in range(0, 5)}
print(f"Comprehension in set: {sqr_set}")
