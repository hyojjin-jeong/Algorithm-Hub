import sys
input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
  queue = deque()
  queue.append((i,j))
  visited[i][j] = 0
  while queue:
    x, y = queue.popleft()
    cnt = visited[x][y]
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == -1 and maps[nx][ny] == 1:
        visited[nx][ny] = cnt + 1
        queue.append((nx,ny)) 
visited = [[-1] * m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if maps[i][j] == 2:
      bfs(i,j)
    elif maps[i][j] == 0:
      visited[i][j] = 0
for i in range(n):
  print(*visited[i])