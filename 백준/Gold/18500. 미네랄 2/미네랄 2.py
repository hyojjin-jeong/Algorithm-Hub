import sys
from collections import deque  #큐 사용
input = sys.stdin.readline

R, C = map(int,input().split())
cave = []
for _ in range(R):
  li = list(input().rstrip())
  cave.append(li)
N = int(input())
hights = list(map(int,input().split()))
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def stick(h,s):
  destroy = -1
  if s == 0:
    for j in range(C):
      if cave[h][j] == "x":
        cave[h][j] = "."
        destroy = j
        break
  else:
    for j in range(C-1,-1,-1):
      if cave[h][j] == "x":
        cave[h][j] = "."
        destroy = j
        break
  new_cluster = []
  if destroy != -1:
    for i in range(4):
      nx, ny = h + dx[i], destroy + dy[i]
      if (0 <= nx < R) and (0 <= ny < C) and cave[nx][ny] == "x":
        new_cluster.append((nx,ny))
  return new_cluster

def bfs(i,j):
  visited = [[False] * C for _ in range(R)]
  q = deque()
  q.append((i,j))
  visited[i][j] = True
  fall_list = []
  while q:
    x, y = q.popleft()
    if x == R-1:
      return
    if cave[x+1][y] == ".":
      fall_list.append((x,y))
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < R) and (0 <= ny < C) and cave[nx][ny] == "x" and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx,ny))
  fall(fall_list,visited)

def fall(f_li, visited):
  fall_dist, flag = 1, True
  while True:
    for fx,fy in f_li:
      if fx+fall_dist == R-1 or (cave[fx+fall_dist+1][fy] == "x" and not visited[fx+fall_dist+1][fy]):
        flag = False
        break
    if not flag:
      break
    fall_dist += 1
  for i in range(R-fall_dist-1,-1,-1):
    for j in range(C):
      if cave[i][j] == "x" and visited[i][j]:
        cave[i][j] = "."
        cave[i+fall_dist][j] = "x"
        
for i in range(N):
  val = stick(R-hights[i],i%2)
  if val:
    for i,j in val:
      bfs(i,j)

for i in cave:
  print("".join(i))
  