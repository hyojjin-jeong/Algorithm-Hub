import sys

input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

N = int(input())
maps = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

def bfs(x,y,count):
  queue = deque([x,y])
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while queue:
    x = queue.popleft()
    y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and maps[nx][ny] == "1":
        visited[nx][ny] = True
        count += 1
        queue.append(nx)
        queue.append(ny)
  return count
answer = []
for i in range(N):
  for j in range(N):
    if maps[i][j] == "1" and not visited[i][j]:
      visited[i][j] = True
      answer.append(bfs(i,j,1))

print(len(answer))
answer = sorted(answer)
for i in range(len(answer)):
  print(answer[i])