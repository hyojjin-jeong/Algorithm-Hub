import sys
input = sys.stdin.readline  #필수로 해놓기
import heapq #다익스트라 알고리즘 사용

N, M, K, X = map(int,input().split())
INF = float('inf')
graphs = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
  A, B = map(int,input().split())
  graphs[A].append((B, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graphs[now]:
      totaldist = dist + i[1]
      if totaldist < distance[i[0]]:
        distance[i[0]] = totaldist
        heapq.heappush(q, (totaldist, i[0]))
dijkstra(X)
ans = []
for i in range(len(distance)):
  if distance[i] == K:
    ans.append(i)
if len(ans) == 0:
  ans.append(-1)
for a in ans:
  print(a)