# import sys

# input = sys.stdin.readline
# li = []
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     li.append([a, b])

# li.sort(key=lambda x: (x[0], x[1]))
# cnt = 0
# while 1:
#     num = 0
#     li1 = []
#     if len(li) < 1:
#         break
#     for i in range(len(li)):
#         if li[i][0] >= num:
#             num = li[i][1]
#         else:
#             li1.append(li[i])
#     cnt += 1
#     li = li1
# print(cnt)

# 시간초과를 어떻게 해결하면 좋을까

import heapq

n = int(input())

li = []

for i in range(n):
    a, b = map(int, input().split())
    li.append([a, b])

li.sort(key=lambda x: x[0])
room = []
heapq.heappush(room, li[0][1])

for i in range(1, n):
    if li[i][0] < room[0]:
        heapq.heappush(room, li[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, li[i][1])

print(len(room))
