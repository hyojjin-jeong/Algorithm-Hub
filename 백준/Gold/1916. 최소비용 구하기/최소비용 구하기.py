import sys
input = sys.stdin.readline
import heapq

INF = float("inf")
N = int(input())
M = int(input())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
  s, e, c = map(int,input().split())
  graphs[s].append((e,c))
start, end = map(int,input().split())
distance = [INF] * (N+1)
q = []
heapq.heappush(q,(0, start))
distance[start] = 0
while q:
  d, now = heapq.heappop(q)
  if distance[now] < d:
    continue
  for next, nd in graphs[now]:
    if distance[next] > d + nd:
      distance[next] = d + nd
      heapq.heappush(q, (distance[next], next))
print(distance[end])