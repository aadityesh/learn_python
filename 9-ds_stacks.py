stack = []  # 1 2 3

stack.append(1)
stack.append(2)
stack.append(3)

last = stack.pop()  # 3
print(stack)  # [1, 2]
top = stack[-1]  # 2, gives IndexError if stack is empty

if not stack:
    print("stack is empty")
