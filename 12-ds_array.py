from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(0, 0)
numbers.pop()  # removes last digit
print(numbers)
