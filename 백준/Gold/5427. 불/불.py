import sys
from typing import Counter

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

TestCase = int(input())

def bfs(xys):
  queue = deque()
  queue = deque((xys))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  while queue:
    x,y = queue.popleft()
    if moves[x][y] != -1 and (fired[x][y] > moves[x][y] or fired[x][y] == -1) and (x == 0 or x == h-1 or y == 0 or y == w-1):
      return moves[x][y]+1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < h) and (0 <= ny < w) and maps[nx][ny] != "#":
        if fired[nx][ny] == -1  and fired[x][y] != -1:
          fired[nx][ny] = fired[x][y] + 1
          queue.append((nx,ny))
        elif moves[x][y] != -1 and moves[nx][ny] == -1 and (fired[nx][ny] > moves[x][y]+1 or fired[nx][ny] == -1):
          moves[nx][ny] = moves[x][y] + 1
          queue.append((nx,ny))     
  return "IMPOSSIBLE"
  
answer = []
for _ in range(TestCase):
  w,h = map(int,input().split())
  maps = [input().rstrip() for _ in range(h)]
  fired = [[-1]*w for _ in range(h)]
  moves = [[-1]*w for _ in range(h)]
  xys = []
  for i in range(h):
    for j in range(w):
      if maps[i][j] == "*":
        xys.append((i,j))
        fired[i][j] = 0
      elif maps[i][j] == "@":
        xys.append((i,j))
        moves[i][j] = 0
  answer.append(bfs(xys))

for i in range(len(answer)):
  print(answer[i])