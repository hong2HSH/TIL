import sys

input = sys.stdin.readline

N = int(input())

dict = dict()

for _ in range(N):
    a = int(input())
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1

num = max(dict.values())
list = []

for i in dict:
    if num == dict[i]:
        list.append(i)

list.sort()
print(list[0])
