import sys

input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

answer = "Hing"
N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0]
dy = [0,1]

visited = [[False] * N for _ in range(N)] 

def bfs(x,y):
  queue = deque([x,y])
  visited[x][y] = True

  while queue:
    nx = queue.popleft()
    ny = queue.popleft()
    n = maps[nx][ny]
    for i in range(2):
      x = nx + dx[i]*n
      y = ny + dy[i]*n

      if (0 <= x < N) and (0 <= y < N) and not visited[x][y]:
        visited[x][y] = True
        queue.append(x)
        queue.append(y)
      

bfs(0,0)

if visited[N-1][N-1]:
  answer = "HaruHaru"

print(answer)