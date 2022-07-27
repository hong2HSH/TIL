import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    N1 = N
    n = set()

    while True :
        for n1 in str(N):
            n.add(n1)
        if len(n) == 10:
            break
        N += N1
    print(f'#{t} {N}')
