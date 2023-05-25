import sys

input = sys.stdin.readline

N = int(input())
dict = {}

for _ in range(N):
    a = input()
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1


for _ in range(N - 1):
    a = input()
    if a in dict:
        dict[a] -= 1
    else:
        dict[a] = 1

for value, key in dict.items():
    if key == 1:
        print(value)
