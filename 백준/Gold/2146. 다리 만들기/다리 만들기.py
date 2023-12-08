import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,count):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True
  maps[x][y] = count
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < N):
        if maps[nx][ny] == 1 and not visited[nx][ny]:
          visited[nx][ny] = True
          maps[nx][ny] = count
          queue.append((nx,ny))
        elif maps[nx][ny] == 0 and lines[x][y] == 0:
          lines[x][y] = 1

def bfs1(a,b):
  queue = deque()
  queue.append((a,b))
  visited[a][b] = 0
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < N):
        if maps[nx][ny] == 0 and (visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y]+1):
          visited[nx][ny] = visited[x][y]+1
          queue.append((nx,ny))
        elif lines[nx][ny] == 1 and maps[a][b] != maps[nx][ny]:
          return visited[x][y]
  return float("inf")
    

visited = [[False]*N for _ in range(N)]
count = 2
lines = [[0]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if maps[i][j] == 1 and not visited[i][j]:
      bfs(i,j,count)
      count += 1
visited = [[-1]*N for _ in range(N)]
answer = []
for i in range(N):
  for j in range(N):
    if lines[i][j] == 1 and visited[i][j] == -1:
      answer.append(bfs1(i,j))
print(min(answer))