import sys
import heapq
input = sys.stdin.readline

N = int(input())
graphs = {i: [0, []] for i in range(1, N+1)}
indegree = {i: 0 for i in range(1,N+1)}
for i in range(N):
  info = list(map(int,input().split()))
  graphs[i+1][0] = info[0]
  if info[1] != 0:
    for j in info[2:]:
      graphs[i+1][1].append(j)
      indegree[j] += 1
answer = 0
q = []
time = {i:0 for i in range(1,N+1)}

for i in range(1, N+1):
  if indegree[i] == 0:
    heapq.heappush(q, i)

while q:
  now = heapq.heappop(q)
  time[now] += graphs[now][0]
  for i in graphs[now][1]:
    indegree[i] -= 1
    time[i] = max(time[i], time[now])
    if indegree[i] == 0:
      heapq.heappush(q,i)
print(max(time.values()))