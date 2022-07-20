import sys

sys.stdin = open("input.txt", "r")

N = int(input())

for i in range(1,N+1):
    n = int(input())
    a = 0
    for j in range(1,n+1):
        if j%2 != 0:
            a = a + j
        else :
            a = a - j
    print('#{} {}'.format(i,a))