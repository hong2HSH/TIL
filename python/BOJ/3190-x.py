from collections import deque

n = int(input())
k = int(input())
map = [[0 for _ in range(n)] for _ in range(n)]

print(map)

for _ in range(k):
    a, b = map(int, input().split())
    map[a - 1][b - 1] = 1

print(map)

l = int(input())
dict = {}
queue = deque((0, 0))

for _ in range(l):
    x, c = input().split()
    dict[int(x)] = c
