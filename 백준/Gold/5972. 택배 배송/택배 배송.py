import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

N, M = map(int,input().split())
INF = float("inf")
graphs = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
  A, B, C = map(int,input().split())
  graphs[A].append((B,C))
  graphs[B].append((A,C))

def dijkstra(start):
  q = []
  heapq.heappush(q,(start,0))
  distance[start] = 0
  while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graphs[now]:
      if dist + i[1] < distance[i[0]]:
        distance[i[0]] = dist + i[1]
        heapq.heappush(q,(i[0], distance[i[0]]))
dijkstra(1)
print(distance[N])