import sys
input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

N, K = map(int,input().split())
maps = [float("inf")] * 100002
dx = [-1,1]
Max = max(N,K)
def bfs(x):
  queue = deque()
  queue.append(x)
  maps[x] = 0
  while maps[K] == float("inf"):
    x = queue.popleft()
    X = x*2
    cnt = maps[x]
    while X < Max+2 and X != 0 and maps[X] > cnt:
      maps[X] = cnt
      queue.append(X)
      X = X*2
    for i in range(2):
      nx = x + dx[i]
      if (0 <= nx < Max+2) and maps[nx] > cnt:
        maps[nx] = min(maps[nx],cnt + 1)
        queue.append(nx)
bfs(N)
print(maps[K])