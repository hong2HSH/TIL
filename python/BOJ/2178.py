from collections import deque

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input())))


def bfs(x, y):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이므로 진행 불가
            if a[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if a[nx][ny] == 1:
                a[nx][ny] = a[x][y] + 1
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return a[n - 1][m - 1]


print(bfs(0, 0))
