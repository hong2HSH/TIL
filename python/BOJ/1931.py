import sys

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append([a, b])
cnt = 1

li.sort(key=lambda x: (x[1], x[0]))
s = li[0][1]
for i in range(1, n):
    if li[i][0] >= s:
        cnt += 1
        s = li[i][1]
print(cnt)
