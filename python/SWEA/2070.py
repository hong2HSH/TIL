import sys

sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(0, n):
    a, b = map(int, input().split())
    print("#%d" % (i+1), end=' ')
    if a < b:
        print("<")
    elif a == b:
        print("=")
    else:
        print(">")