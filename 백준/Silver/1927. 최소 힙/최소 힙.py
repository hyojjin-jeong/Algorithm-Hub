import sys
input = sys.stdin.readline
import heapq #다익스트라 알고리즘, 우선순위 큐 사용

N = int(input())
q = []
for _ in range(N):
  x = int(input())
  if x == 0:
    if q:
      print(heapq.heappop(q))
    else:
      print(0)
  else:
    heapq.heappush(q,x)