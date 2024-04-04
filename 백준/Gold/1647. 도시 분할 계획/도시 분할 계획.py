import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lines = [list(map(int,input().split())) for _ in range(M)]
lines.sort(key=lambda x : x[2])
parent = [i for i in range(N+1)]
dist, cnt, Mdist = 0, 0, 0

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

for a, b, v in lines:
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a
    dist += v
    cnt += 1
    Mdist = v
    if cnt > N - 1:
      break
print(dist - Mdist)