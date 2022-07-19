import sys

sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(0, n):
    a, b = map(int, input().split())
    print("#%d" % (i+1), end=' ')
    print(int(a/b), a%b)