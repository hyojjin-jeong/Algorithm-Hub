from sys import stdin
input = stdin.readline
from collections import deque  #큐 사용

T = int(input())
def t_sort():
  q = deque()
  for i in range(1,N+1):
    if indegree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    ans[now] += time[now]
    for next in graph[now]:
      ans[next] = max(ans[next], ans[now])
      indegree[next] -= 1
      if indegree[next] == 0:
        q.append(next)
for _ in range(T):
  N, K = map(int,input().split())
  time = [0] + list(map(int,input().split()))
  graph = {i: [] for i in range(1,N+1)}
  indegree = [0] * (N+1)
  for _ in range(K):
    X, Y = map(int,input().split())
    graph[X].append(Y)
    indegree[Y] += 1
  W = int(input())
  ans = [0] * (N+1)
  t_sort()
  print(ans[W])