import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    A = W * P
    B = Q
    if W > R :
        B += (W - R) * S
    print('#' + str(i), end = " ") 

    if A > B :
        print(B)
    else :
        print(A)