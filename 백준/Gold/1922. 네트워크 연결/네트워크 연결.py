import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

N = int(input())
M = int(input())
lines = [list(map(int,input().split())) for _ in range(M)]
lines.sort(key=lambda x : x[2])
parent = [i for i in range(N+1)]
dist, cnt = 0, 0

def find(x):
  if x != parent[x]:
    parent[x] = find(parent[x])
  return parent[x]

for a, b, c in lines:
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a
    dist += c
    cnt += 1
    if cnt > N - 1:
      break
print(dist)