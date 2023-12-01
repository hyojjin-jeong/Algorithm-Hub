import sys
input = sys.stdin.readline #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

M,N = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(M)]

visited = [[-1] * N for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  if x == M-1 and y == N-1:
    return 1
  if visited[x][y] != -1:
    return visited[x][y]

  ways = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < M) and (0 <= ny < N) and (maps[nx][ny] < maps[x][y]):
      ways += dfs(nx,ny)
  visited[x][y] = ways
  return visited[x][y]

print(dfs(0,0))