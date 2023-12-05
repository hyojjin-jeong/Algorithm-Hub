import sys

input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

M,N,K = map(int,input().split())
visited = [[0]*N for _ in range(M)]

for _ in range(K):
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      visited[i][j] = 1

def bfs(i,j):
  queue = deque([i,j])
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  count = 1
  while queue:
    y = queue.popleft()
    x = queue.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if (0 <= ny < M) and (0 <= nx < N) and visited[ny][nx] == 0:
        visited[ny][nx] = 1
        count += 1
        queue.append(ny)
        queue.append(nx)
  return count

answer = []
for i in range(M):
  for j in range(N):
    if visited[i][j] == 0:
      visited[i][j] = 1
      answer.append(bfs(i,j))
print(len(answer))
print(*sorted(answer))