from sys import stdin
input = stdin.readline
from collections import defaultdict #dict 초기화
import heapq #다익스트라 알고리즘 사용

INF = float("inf")
N, M = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
  A, B, C = map(int,input().split())
  graph[A].append((B,C))
  graph[B].append((A,C))

def dijkstra(start):
  q = []
  heapq.heappush(q, (start,0))
  dist = {i: INF for i in range(1,N+1)}
  dist[start] = 0
  while q:
    now, d = heapq.heappop(q)
    for next, n_d in graph[now]:
      if dist[next] > dist[now] + n_d:
        dist[next] = dist[now] + n_d
        if answer[next]:
          answer[next].pop()
        answer[next].append((now,next))
        heapq.heappush(q, (next,dist[next]))

answer = [[] for _ in range(N+1)]
dijkstra(1)
list = []
cnt = 0
for ans in answer:
  if ans:
    cnt += len(ans)
    for a in ans:
      list.append(a)
print(cnt)
for li in list:
  print(*li)