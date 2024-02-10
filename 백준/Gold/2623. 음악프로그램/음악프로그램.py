import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
graphs = {i: [] for i in range(1,N+1)}
indegree = {i: 0 for i in range(1,N+1)}
answer = []
q = []
for _ in range(M):
  line = list(map(int,input().split()))
  for i in range(1, len(line)-1):
    graphs[line[i]].append(line[i+1])
    indegree[line[i+1]] += 1

for i in range(1,N+1):
  if indegree[i] == 0:
    heapq.heappush(q, i)

while q:
  tmp = heapq.heappop(q)
  answer.append(tmp)
  for i in graphs[tmp]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(q, i)

if len(answer) == N:
  for a in answer:
    print(a)
else:
  print(0)