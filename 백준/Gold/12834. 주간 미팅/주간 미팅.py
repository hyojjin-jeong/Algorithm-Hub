from sys import stdin
input = stdin.readline
from collections import defaultdict #dict 초기화
import heapq #다익스트라 알고리즘 사용

INF = float("inf")
N, V, E = map(int,input().split())
A, B = map(int,input().split())
house = list(map(int,input().split()))
graph = defaultdict(list)
for _ in range(E):
  a, b, len = map(int,input().split())
  graph[a].append((b,len))
  graph[b].append((a,len))

def dijkstra(start):
  q = []
  heapq.heappush(q, (start, 0))
  d = [INF] * (V+1)
  d[start] = 0
  while q:
    cur, dist = heapq.heappop(q)
    for next,n_d in graph[cur]:
      if d[next] > dist + n_d:
        d[next] = dist + n_d
        heapq.heappush(q, (next, d[next]))
  return d

answer = 0
for i in house:
  dist = dijkstra(i)
  if dist[A] == INF:
    answer += -1
  else:
    answer += dist[A]
  if dist[B] == INF:
    answer += -1
  else:
    answer += dist[B]
print(answer)