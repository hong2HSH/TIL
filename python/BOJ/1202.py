# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# li = {}
# weight = []

# for _ in range(n):
#     m, v = map(int, input().split())
#     key = m
#     value = v
#     li[key] = value
# for _ in range(k):
#     c = int(input())
#     weight.append(c)
# li = sorted(li.items(), key=lambda x: x[1], reverse=True)
# weight.sort()
# money = 0
# for i in weight:
#     for j in li:
#         if i >= j[0]:
#             money += j[1]
#             li.remove(j)
#             break

# print(money)

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
li = []
for _ in range(N):
    heapq.heappush(li, list(map(int, sys.stdin.readline().split())))
weight = []
for _ in range(K):
    weight.append(int(sys.stdin.readline()))
weight.sort()

money = 0
tmp_li = []
for bag in weight:
    while li and bag >= li[0][0]:
        heapq.heappush(tmp_li, -heapq.heappop(li)[1])
    if tmp_li:
        money -= heapq.heappop(tmp_li)
    elif not li:
        break
print(money)
