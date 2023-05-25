N, M = map(int, input().split())

cnt = 0

for _ in range(M):
    a = int(input())
    a1 = list(map(int, input().split()))
    b = sorted(a1, reverse=True)
    if a1 == b:
        cnt += 1
        continue
    else:
        continue
if cnt == M:
    print("Yes")
else:
    print("No")
