numbers = [1, 2, 3, 4]
# numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 5:
        print("Target found")
        break
else:
    print("Loop completed fullly and target not found")

cnt = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        cnt += 1
else:
    print(f"{cnt} even nos were printed")
