import sys
input = sys.stdin.readline
import heapq #다익스트라 알고리즘, 우선순위 큐 사용

N = int(input())
cup = []
for _ in range(N):
  d, c = map(int,input().split())
  cup.append((d,c))
cup = sorted(cup, key=lambda x : x[0])
q = []
for d, c in cup:
  heapq.heappush(q, c)
  if len(q) > d:
    heapq.heappop(q)
print(sum(q))