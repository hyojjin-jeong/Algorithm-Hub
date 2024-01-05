import sys
input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

N = int(input())
M = int(input())
graphs = [[] for _ in range(N+1)]
for i in range(N):
  connections = list(map(int,input().split()))
  for c in range(len(connections)):
    if connections[c] == 1:
      graphs[i+1].append(c+1)
plan = list(map(int,input().split()))

def bfs(start,end):
  q = deque()
  q.append(start)
  visited[start] = True
  while q:
    x = q.popleft()
    if x == end:
      return 1
    for node in graphs[x]:
      if not visited[node]:
        visited[node] = True
        q.append(node)
  return 0
ans = []
for i in range(len(plan)-1):
  visited = [False for _ in range(N+1)]
  ans.append(bfs(plan[i],plan[i+1]))
if 0 in ans:
  print("NO")
else:
  print("YES")