import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
weight = list(map(int,input().split()))
crane.sort()
weight.sort(reverse=True)
cnt = 0
if max(crane) < max(weight):
    print(-1)
else:
    while 1:
        if weight == []:
            break
        for i in range(n):
            for j in range(len(weight)):
                if weight[j] <= crane[i]:
                    weight.remove(weight[j])
                    break
        cnt += 1
    print(cnt)