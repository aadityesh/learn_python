dict_var = {
    "name": "AJ",
    "age": 22
}

print(dict_var["age"])
dict_var["phone_num"] = 9876890799  # Add
print(dict_var)

print(dict_var.get("name", -1))  # Does not return keyError
del dict_var["phone_num"]  # Delete

# List comprehension for Dict

num_dict = {x: x ** 2 for x in range(0, 5)}
print(num_dict)
print(num_dict)

# Unpacking dict
first = {"x": 1}
second = {"y": 2}
third = {**first, **second, "z": 3}
print(third)

#
ques = "This is a common question"
hash = {}

for char in ques:
    value = hash.get(char, 0) + 1
    hash[char] = value

print(hash)
