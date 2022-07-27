import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(T) :
    a, b = input().split()
    print(int(a)+int(b))
