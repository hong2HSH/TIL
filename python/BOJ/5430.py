import sys
from collections import deque

t = int(input())

for _ in range(t):
    li = sys.stdin.readline().rstrip()
    n = int(input())
    num = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    a = 1
    for i in range(len(li)):
        if li[i] == "R":
            num.reverse()
        elif li[i] == "D":
            if len(num) == 0:
                a = 0
                break
            num.popleft()
    if a == 0 or n == 0:
        print("error")
    else:
        print(list(map(int, num)))
