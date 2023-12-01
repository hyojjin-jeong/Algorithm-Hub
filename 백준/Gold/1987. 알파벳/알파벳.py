import sys
input = sys.stdin.readline #필수로 해놓기

R,C = map(int,input().split())

board = [list(input().rstrip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
alphas = set()
alphas.add(board[0][0])

def dfs(x,y,count):
  global ans
  ans = max(ans, count)
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < R) and (0 <= ny < C):
      if not board[nx][ny] in alphas:
        alphas.add(board[nx][ny])
        dfs(nx,ny,count+1)
        alphas.remove(board[nx][ny])

dfs(0,0,1)
print(ans)