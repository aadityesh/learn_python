from collections import deque

que = deque([])

que.append(1)
que.append(2)
que.append(3)

print(que)
print(f"last elem without popping: {que[-1]}")

first = que.popleft()
last = que.pop()

print(f"first: {first}")
print(f"last: {last}")
print(f"q: {que}")

if not que:
    print("que is empty")
