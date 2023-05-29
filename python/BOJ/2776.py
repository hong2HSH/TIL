import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a = int(input())
    li1 = set(map(int, input().split()))
    b = int(input())
    li2 = list(map(int, input().split()))

    for i in li2:
        if i in li1:
            print(1)
        else:
            print(0)
