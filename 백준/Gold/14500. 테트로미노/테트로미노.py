import sys
input = sys.stdin.readline  # 필수로 해놓기

N, M = map(int,input().split())
papper = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,cnt,total):
  global answer
  if cnt == 4:
    answer = max(answer, total)
    return
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
        visited[nx][ny] = True
        dfs(nx,ny,cnt+1,total+papper[nx][ny])
        visited[nx][ny] = False

def h(x,y):
  global answer
  for i in range(4):
    start = papper[x][y]
    for j in range(3):
      k = (i+j) % 4
      nx = x + dx[k]
      ny = y + dy[k]
      if not (0 <= nx < N and 0 <= ny < M):
        start = 0
        break
      start += papper[nx][ny]
    answer = max(answer, start)
    
answer = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
  for j in range(M):
    visited[i][j] = True
    dfs(i,j,1,papper[i][j])
    visited[i][j] = False
    h(i,j)
print(answer)