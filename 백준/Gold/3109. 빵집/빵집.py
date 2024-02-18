import sys
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
input = sys.stdin.readline

R, C = map(int,input().split())
map = [list(input().rstrip()) for _ in range(R)]
dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x,y):
  if y == C-1:
    return True
  for i in range(3):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < R) and (0 <= ny < C) and map[nx][ny] == ".":
      map[nx][ny] = "x"
      if dfs(nx,ny):
        return True
  return False

answer = 0
for i in range(R):
  if dfs(i,0):
    answer += 1

print(answer)