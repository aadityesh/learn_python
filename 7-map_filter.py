tuple_ls = [
    ("p1", 10),
    ("p1", 9),
    ("p1", 5),
]

prices = []
for obj in tuple_ls:
    prices.append(obj[1])

prices = map(lambda obj: obj[1], tuple_ls)
print(list(prices))

filtered_prices = filter(lambda obj: obj[1] >= 7, tuple_ls)

print(list(filtered_prices))


# Filter using List Comprehension
ls = [obj[1] for obj in tuple_ls if obj[1] > 6]
print(f"Filter using List Comprehension: {ls}")
