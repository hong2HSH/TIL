import sys
import heapq

input = sys.stdin.readline

n = int(input())
li = []  # 묶음
cnt = 0  # 비교횟수

for _ in range(n):
    a = int(input())
    heapq.heappush(li, a)
while 1:
    if len(li) == 1:
        break
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    cnt += a + b
    heapq.heappush(li, a + b)
print(cnt)
