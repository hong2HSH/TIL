T = int(input())

for _ in range(T):
    n, k = map(int(input().split()))
    time = list(map(int(input().split())))
    li = [[] for _ in range(n + 1)]

    for _ in range(k):
        a, b = map(int, input().split())
        if b not in li:
            time[b - 1] += time[a - 1]
            li.append(b)
        else:
            time[b - 1] += a

## 각 경로를 모두들린 값 중 최대값
