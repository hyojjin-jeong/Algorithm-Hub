import sys

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

M, N, H = map(int, input().split())
tomatos = [[list(map(int,
                     input().split())) for _ in range(N)] for _ in range(H)]


def bfs(tts):
  queue = deque((tts))
  dx = [-1, 1, 0, 0, 0, 0]
  dy = [0, 0, -1, 1, 0, 0]
  dz = [0, 0, 0, 0, -1, 1]
  n = 0
  while queue:
    x, y, z = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      n = visited[x][y][z]
      if (0 <= nx < H) and (0 <= ny < N) and (
          0 <= nz <
          M) and visited[nx][ny][nz] == -1 and tomatos[nx][ny][nz] == 0:
        visited[nx][ny][nz] = n + 1
        tomatos[nx][ny][nz] = 1
        queue.append((nx, ny, nz))
  return n


def tomato_count(tomatos):
  count = 0
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if tomatos[i][j][k] == 0:
          count += 1
  return count


if tomato_count(tomatos) == 0:
  answer = 0

visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
tts = []
for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomatos[i][j][k] == 1 and visited[i][j][k] == -1:
        visited[i][j][k] = 0
        tts.append((i, j, k))

answer = bfs(tts)

if tomato_count(tomatos) != 0:
  answer = -1

print(answer)
