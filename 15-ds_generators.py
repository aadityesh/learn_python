from sys import getsizeof

nums = (x * 2 for x in range(1, 6))  # generator

# print(nums)
# for num in nums:
#     print(num, end=" ")

print(f"sizeof in bytes: {getsizeof(nums)}")
