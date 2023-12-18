import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

R, C, K = map(int, input().split())
maps = [input().rstrip() for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
def dfs(x,y,cnt):
  global ans
  if x == 0 and y == C-1 and cnt == K:
      ans += 1
  else:
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < R) and (0 <= ny < C) and maps[nx][ny] == "." and not visited[nx][ny]:
        visited[nx][ny] = True
        dfs(nx,ny,cnt+1)
        visited[nx][ny] = False

visited = [[False] * C for _ in range(R)]
dfs(R-1,0,1)
print(ans)

