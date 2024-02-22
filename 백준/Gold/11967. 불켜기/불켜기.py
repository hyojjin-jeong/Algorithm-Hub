import sys
from collections import deque  #큐 사용
input = sys.stdin.readline

N, M = map(int,input().split())
switch = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
  x, y, a, b = map(int,input().split())
  switch[x][y].append((a,b))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
          
def on(i,j):
  global cnt
  q = deque()
  q.append((i,j))
  bright[i][j] = True
  visited[i][j] = True
  while q:
    x, y = q.popleft()
    for a,b in switch[x][y]:
      if not bright[a][b]:
        bright[a][b] = True
        cnt += 1
        for k in range(4):
          na = a + dx[k]
          nb = b + dy[k]
          if (1 <= na <= N) and (1 <= nb <= N) and visited[na][nb]:
            q.append((na,nb))
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (1 <= nx <= N) and (1 <= ny <= N) and not visited[nx][ny] and bright[nx][ny]:
        visited[nx][ny] = True
        q.append((nx,ny))
        
cnt = 0
bright = [[False for _ in range(N+1)] for _ in range(N+1)]
visited = [[False for _ in range(N+1)] for _ in range(N+1)]
on(1,1)
print(cnt+1)