from sys import stdin
input = stdin.readline
from collections import defaultdict #dict 초기화
import heapq #다익스트라 알고리즘 사용

T = int(input())
INF = float("inf")
def dijkstra(start):
  q = []
  heapq.heappush(q,(start,0))
  dist[start] = 0
  while q:
    now, d = heapq.heappop(q)
    for next,n_d in secrets[now]:
      if dist[next] > d + n_d:
        dist[next] = d + n_d
        heapq.heappush(q,(next,dist[next]))
for _ in range(T):
  N, M = map(int,input().split())
  secrets = defaultdict(list)
  for _ in range(M):
    a, b, c = map(int,input().split())
    secrets[a].append((b,c))
    secrets[b].append((a,c))
  K = int(input())
  friends = list(map(int,input().split()))
  total = INF
  answer = 0
  for i in range(1,N+1):
    s = 0
    dist = [INF] * (N+1)
    dijkstra(i)
    for f in friends:
      s += dist[f]
    if total > s:
      total = s
      answer = i
  print(answer)