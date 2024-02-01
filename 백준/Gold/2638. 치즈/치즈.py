import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
papper = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def inner(a,b):
  q = deque()
  ex = []
  ex.append((a,b))
  q.append((a,b))
  visited[a][b] = True
  t = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < M):
        if not visited[nx][ny] and papper[nx][ny] == 0:
          visited[nx][ny] = True
          q.append((nx,ny))
          ex.append((nx,ny))
      else:
        t = 1
  if t == 0:
    inair.extend(ex)

def bfs(a,b):
  q = deque()
  q.append((a,b))
  visited[a][b] = True
  while q:
    x, y = q.popleft()
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < M):
        if papper[nx][ny] == 0 and (nx,ny) not in inair:
          cnt += 1
        elif papper[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = True
          q.append((nx,ny))
      else:
        cnt += 1
    if cnt >= 2:
      erase.append((x,y))
answer = 0
while True:
  visited = [[False] * M for _ in range(N)]
  inair = []
  for i in range(N):
    for j in range(M):
      if papper[i][j] == 0 and not visited[i][j]:
        inner(i,j)
  
  visited = [[False] * M for _ in range(N)]
  erase = []
  for i in range(N):
    for j in range(M):
      if papper[i][j] == 1 and not visited[i][j]:
        bfs(i,j)
  if len(erase) == 0:
    break
  for x, y in erase:
    papper[x][y] = 0
  answer += 1
print(answer)