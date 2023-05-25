import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a = set()
b = set()

for _ in range(N):
    a.add(input())

for i in range(M):
    b.add(input())

ans = sorted(list(a & b))

print(len(ans))

for k in ans:
    print(k, end="")
