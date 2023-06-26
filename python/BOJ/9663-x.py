n = int(input())
map = [[0 for _ in range(n)] for _ in range(n)]
print(map)
cnt = 0
for i in range(n):
    for j in range(n):
        if map[i][j] == 0:
            map[i:][j] = 1
            cnt += 1
            break
        else:
            continue
print(map)
