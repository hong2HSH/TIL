import heapq

n = int(input())

li = list(map(int, input().split()))

li.sort()
num = 1

for i in li:
    if num < i:
        break
    num += i
print(num)
