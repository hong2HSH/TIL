N, M = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
a = int(input())
for i in range(a):
    i, j, x, y = map(int, input().split())
    print(str(a[x][y] - a[x][j - 1] - a[i - 1][y] + a[i - 1][j + 1]))
