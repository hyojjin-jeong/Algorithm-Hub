import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

N, M = map(int,input().split())
INF = float('inf')
graphs = [[] for _ in range(N+1)]
for i in range(M):
  A, B = map(int,input().split())
  graphs[A].append((i,B))
  graphs[B].append((i,A))
distance = [INF for _ in range(N+1)]

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for node in graphs[now]:
      time = node[0]
      if (dist-time) % M == 0:
        time += ((dist-time)//M) * M
      else:
        time += ((dist-time)//M + 1) * M
      time += 1
      if time < distance[node[1]]:
        distance[node[1]] = time
        heapq.heappush(q, (time, node[1]))
dijkstra(1)
print(distance[-1])