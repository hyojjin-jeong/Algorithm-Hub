import sys

input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

TestCase = int(input())
def bfs(x,y):
  queue = deque([x,y])
  dx = [-1,1,-2,2,-2,2,-1,1]
  dy = [-2,-2,-1,-1,1,1,2,2]
  
  while queue:
    x = queue.popleft()
    y = queue.popleft()
    if x == x2 and y == y2:
      return visited[x][y]
    n = visited[x][y]
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < I) and (0 <= ny < I) and visited[nx][ny] == -1:
        visited[nx][ny] = n+1
        queue.append(nx)
        queue.append(ny)
  return 0
        
ans = []
for _ in range(TestCase):
  I = int(input())
  x1,y1 = map(int, input().split())
  x2,y2 = map(int, input().split())
  visited = [[-1]*I for _ in range(I)]
  visited[x1][y1] = 0
  ans.append(bfs(x1,y1))

for i in range(len(ans)):
  print(ans[i])