import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

N, M, X = map(int,input().split())
INF = float('inf')
graphs = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
  start, end, time = map(int,input().split())
  graphs[start].append((end, time))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graphs[now]:
      finaltime = dist + i[1]
      if finaltime < distance[i[0]]:
        distance[i[0]] = finaltime
        heapq.heappush(q, (finaltime, i[0]))
ans = []
for i in range(1,N+1):
  distance = [INF] * (N+1)
  dijkstra(i)
  Time = distance[X]
  distance = [INF] * (N+1)
  dijkstra(X)
  Time += distance[i]
  ans.append(Time)
print(max(ans))
