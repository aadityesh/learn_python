ls = ["a", "b", "c"]
matrix = [
    [0, 1],
    [2, 3],
    [4, 5],
]

recurring_elem_ls = [1] * 5
print(recurring_elem_ls)

a = ('a', 'b', 'c')
b = ["c", "d", "e"]
concat_ls = list(a) + b
print(concat_ls)

one_to_ten_ls = list(range(1, 11))
alphabet_list = list("alphabet")
print(one_to_ten_ls)
print(alphabet_list)


num = [1, 2, 3, 4, 5]
a, b, *other = num
print(a, " ", b, " ", other)

num = [5, 6, 1, 2, 1, 0]
print(sorted(num))

tuple_ls = [
    ("p1", 10),
    ("p1", 9),
    ("p1", 5),
]


def customSort(tuple_ls):
    return tuple_ls[1]


print(tuple_ls)
# tuple_ls.sort(key=customSort)
tuple_ls.sort(key=lambda ls: ls[1])
print(tuple_ls)


# List Comprehension
prices_ls = [item[1] for item in tuple_ls]
print("List comprehension")
print(prices_ls)

# Unpacking list
values = [*range(1, 4), *"Hello"]  # * unpacks individual elements
print(values)
