point = 1,      # tuple
point = 1, 2     # tuple
point = (1, 2)   # tuple

# point[0] = 3 # Error

# Tuple Unpacking
x, y = point  # 1, 2

# (1, 2, 3, 4)
point_concat = (1, 2) + (3, 4)

# (1, 2, 1, 2, 1, 2)
point_multi = (1, 2) * 3
print(point_multi)

# ('g', 'o', 'o', 'd')
string_tp = tuple("good")
print(string_tp)
