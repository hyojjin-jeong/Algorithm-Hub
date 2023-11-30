import sys
input = sys.stdin.readline #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

N = int(input())
arr = [list(input()) for _ in range(N)]

visited =[[False]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  visited[x][y] = True
  color = arr[x][y]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < N) and (0 <= ny < N):
      if not visited[nx][ny]:
        if arr[nx][ny] == color:
          dfs(nx,ny)

ans3,ans2 = 0,0

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      dfs(i,j)
      ans3 += 1

for i in range(N):
  for j in range(N):
    if arr[i][j] == 'R':
      arr[i][j] = 'G'

visited =[[False]*N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      dfs(i,j)
      ans2 += 1

print(ans3,ans2)