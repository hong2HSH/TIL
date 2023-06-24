# import sys

# input = sys.stdin.readline
# n = int(input())
# plus = []
# minus = []
# li = list(map(int, input().split()))

# for i in li:
#     if i > 0:
#         plus.append(i)
#     else:
#         minus.append(i)

# sum = plus[0] + minus[0]
# li = []

# for i in plus:
#     for j in minus:
#         if i + j < abs(sum):
#             sum = i + j
#             li = [j, i]
# print(" ".join(map(str, li)))

import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))
li.sort()
sum = abs(li[0] + li[1])
left = 0
right = n - 1
ans = [li[0], li[1]]

while left < right:
    sum1 = li[left] + li[right]
    if abs(sum1) < sum:
        sum = abs(sum1)
        ans = [li[left], li[right]]
    if sum1 < 0:
        left += 1
    else:
        right -= 1
print(ans[0], ans[1])
