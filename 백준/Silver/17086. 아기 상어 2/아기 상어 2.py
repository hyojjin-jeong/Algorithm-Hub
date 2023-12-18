import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

N, M = map(int,input().split())
boxes = [list(map(int,input().split())) for _ in range(N)]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  dx = [-1,0,1,-1,1,-1,0,1]
  dy = [1,1,1,0,0,-1,-1,-1]
  while queue:
    x,y = queue.popleft()
    cnt = visited[x][y]
    if boxes[x][y] == 1:
      return cnt - 1
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < M) and visited[nx][ny] == 0:
        visited[nx][ny] = cnt + 1
        queue.append((nx,ny))
  return 0

ans = []
for i in range(N):
  for j in range(M):
    if boxes[i][j] == 0:
      visited = [[0]*M for _ in range(N)]
      visited[i][j] = 1
      ans.append(bfs(i,j))
print(max(ans))