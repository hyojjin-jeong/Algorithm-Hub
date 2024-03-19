import sys
input = sys.stdin.readline
import heapq #다익스트라 알고리즘, 우선순위 큐 사용

INF = float("inf")
V, E = map(int,input().split())
K = int(input())
graphs = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int,input().split())
  graphs[u].append((v,w))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  answer[start] = 0
  while q:
    d, now = heapq.heappop(q)
    if answer[now] < d:
      continue
    for next, w in graphs[now]:
      if answer[next] > d + w:
        answer[next] = d + w
        heapq.heappush(q, (answer[next], next))
        
answer = [INF] * (V+1)
dijkstra(K)
for i in range(1,V+1):
  if answer[i] == INF:
    print("INF")
  else:
    print(answer[i])