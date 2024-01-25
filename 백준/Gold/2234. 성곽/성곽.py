import sys
input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

N, M = map(int,input().split())
types = {
  0: [0,0,0,0],
  1: [0,1,0,0],
  2: [0,0,0,1],
  3: [0,1,0,1],
  4: [1,0,0,0],
  5: [1,1,0,0],
  6: [1,0,0,1],
  7: [1,1,0,1],
  8: [0,0,1,0],
  9: [0,1,1,0],
  10: [0,0,1,1],
  11: [0,1,1,1],
  12: [1,0,1,0],
  13: [1,1,1,0],
  14: [1,0,1,1],
  15: [1,1,1,1]
}
maps = [list(map(int,input().split())) for _ in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a,b):
  q = deque()
  q.append((a,b))
  w = 1
  visited[a][b] = w
  w += 1
  room[a][b] = cnt
  while q:
    x, y = q.popleft()
    num = maps[x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < M) and (0 <= ny < N) and types[num][i] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = w
        w += 1
        room[nx][ny] = cnt
        q.append((nx,ny))
    if len(q) == 0:
      return visited[x][y]
rooms = []
visited = [[0] * N for _ in range(M)]
room = [[-1] * N for _ in range(M)]
cnt = 0
for i in range(M):
  for j in range(N):
    if visited[i][j] == 0:
      rooms.append(bfs(i,j))
      cnt += 1
sum = 0
for i in range(M):
  for j in range(N):
    for k in range(4):
      ni = i + dx[k]
      nj = j + dy[k]
      if (0 <= ni < M) and (0 <= nj < N) and room[i][j] != room[ni][nj]:
        sum = max(sum, rooms[room[i][j]] + rooms[room[ni][nj]])
print(len(rooms))
print(max(rooms))
print(sum)