import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

N, D = map(int,input().split())
INF = float('inf')
graphs = [[] for _ in range(D+1)]
for i in range(D):
  graphs[i].append((i+1, 1))
for _ in range(N):
  start, end, length = map(int,input().split())
  if end > D:
    continue
  graphs[start].append((end,length))

distance = [INF for _ in range(D+1)]

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graphs[now]:
      if dist + i[1] < distance[i[0]]:
        distance[i[0]] = dist + i[1]
        heapq.heappush(q, (dist + i[1], i[0]))
dijkstra(0)
print(distance[D])