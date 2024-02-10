import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
first = {i: [] for i in range(1,N+1)}
indegree = {i: 0 for i in range(1,N+1)}
q = []
answer = []
for _ in range(M):
  A, B = map(int,input().split())
  first[A].append(B)
  indegree[B] += 1

for i in range(1,N+1):
  if indegree[i] == 0:
    heapq.heappush(q, i)

while q:
  tmp = heapq.heappop(q)
  answer.append(tmp)
  for i in first[tmp]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(q, i)

print(*answer)