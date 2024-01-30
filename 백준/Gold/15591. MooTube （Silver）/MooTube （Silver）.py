import sys
input = sys.stdin.readline  # 필수로 해놓기
from collections import deque  #큐 사용

N, Q = map(int,input().split())
INF = float("inf")
graphs = [[] for _ in range(N+1)]
for _ in range(N-1):
  p, q, r = map(int,input().split())
  graphs[p].append((q,r))
  graphs[q].append((p,r))

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True
  while q:
    now = q.popleft()
    for i in graphs[now]:
      next = i[0]
      next_d = i[1]
      if not visited[next]:
        visited[next] = True
        dist_li[next] = min(dist_li[now],next_d)
        q.append(next)
      
for _ in range(Q):
  k, v = map(int,input().split())
  dist_li = {i: INF for i in range(1,N+1)}
  visited = {i: False for i in range(1,N+1)}
  bfs(v)
  ans = 0
  for key, value in dist_li.items():
    if value >= k:
      ans += 1
  print(ans - 1)