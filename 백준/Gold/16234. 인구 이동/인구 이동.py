import sys

input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

N, L, R = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]


def bfs(x, y):
  q = deque()
  q.append((x, y))
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  temp = []
  temp.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    num = grounds[x][y]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and (
          L <= abs(num - grounds[nx][ny]) <= R):
        visited[nx][ny] = True
        q.append((nx, ny))
        temp.append((nx, ny))
  return temp

answer = 0
while True:
  cnt = 0
  visited = [[False] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        ans = bfs(i, j)
        if len(ans) > 1:
          cnt = 1
          newNum = sum([grounds[x][y] for x, y in ans]) // len(ans)
          for x, y in ans:
            grounds[x][y] = newNum
  if cnt == 0:
    break
  answer += 1
print(answer)
