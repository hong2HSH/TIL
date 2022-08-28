import sys
input = sys.stdin.readline

N = int(input())
li1 = list(map(int,input().split()))
M = int(input())
li2 = list(map(int,input().split()))
ans = []

for i in li2:
    a = li1.count(i)
    ans.append(a)
print(*ans)