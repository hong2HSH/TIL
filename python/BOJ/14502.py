from collections import deque

n,m = map(int,input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0

for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs():
    queue = deque()
    t_graph = graph
    for i in range(n):
        for j in range(m):
            if t_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if t_graph[nx][ny] == 0:
                t_graph[nx][ny] = 2
                queue.append((nx,ny))
    cnt = 0

    
    for i in range(n):
        cnt += t_graph[i].count(0)

    ans = max(ans,cnt)

    def wall(cnt):
        if cnt == 3:
            bfs()
            return
        
        for i in range(n):
            for j in range(m):
                if gra