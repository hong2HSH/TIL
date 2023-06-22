n = int(input())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

for i in range(1, len(li)):
    for j in range(i + 1):
        if j == 0:
            li[i][0] += li[i - 1][0]
        elif j == i:
            li[i][j] += li[i - 1][j - 1]
        else:
            li[i][j] += max(li[i - 1][j], li[i - 1][j - 1])
print(max(li[n - 1]))
