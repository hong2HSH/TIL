paper = [[0 for _ in range(101)] for _ in range(101)]
ans = paper
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            ans[i][j] = 1
cnt = 0
for k in paper:
    cnt += k.count(1)

print(cnt)
