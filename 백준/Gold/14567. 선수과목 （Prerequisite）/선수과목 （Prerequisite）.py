from sys import stdin
input = stdin.readline
from collections import defaultdict #dict 초기화
from collections import deque  #큐 사용

N, M = map(int,input().split())
indegree = [0] * (N+1)

graph = defaultdict(list)
for _ in range(M):
  A, B = map(int,input().split())
  graph[A].append(B)
  indegree[B] += 1

def t_sort():
  q = deque()
  for i in range(1,N+1):
    if indegree[i] == 0:
      q.append((i,1))
  while q:
    now, num = q.popleft()
    answer[now] = num
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append((i, num+1))
    
answer = [0] * (N+1)
t_sort()
print(*answer[1:])