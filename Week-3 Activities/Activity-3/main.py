# Source : https://www.geeksforgeeks.org/stack-in-python/

from collections import deque

stack = deque()

for i in range(11):

    stack.append(i**2)

stack.popleft()
print(stack)

for i in range (11):
    stack.popleft()
    print(stack)

sorted_deque = sorted( deque([8, 93, 32, 90, 42, 93, 51, 14, 41]) )
print( sorted_deque )

