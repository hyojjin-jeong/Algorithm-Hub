import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

def bfs(i,j,visited):
    q = deque()
    q.append((i,j))
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] and maps[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx,ny))

def wall(cnt):
    global answer
    if cnt == 3:
        visited = [[False] * M for _ in range(N)]
        for a in range(N):
            for b in range(M):
                if maps[a][b] == 2 and not visited[a][b]:
                    bfs(a,b,visited)
        safe = 0
        for a in range(N):
            for b in range(M):
                if maps[a][b] == 0 and not visited[a][b]:
                    safe += 1
        answer = max(answer, safe)
        return
    else:
        for a in range(N):
            for b in range(M):
                if maps[a][b] == 0:
                    maps[a][b] = 1
                    wall(cnt+1)
                    maps[a][b] = 0

answer = 0
wall(0)
print(answer)