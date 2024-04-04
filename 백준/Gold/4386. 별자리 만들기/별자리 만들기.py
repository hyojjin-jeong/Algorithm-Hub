import sys
input = sys.stdin.readline
import math
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

n = int(input())
star = [list(map(float,input().split())) for _ in range(n)]
lines = []
for i in range(n):
  for j in range(i+1,n):
    x = (star[i][0] - star[j][0])**2
    y = (star[i][1] - star[j][1])**2
    lines.append((i,j,math.sqrt(x + y)))
lines.sort(key=lambda x : x[2])
parent = [i for i in range(n)]
dist, cnt = 0, 0

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]


for a, b, v in lines:
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a
    dist += v
    cnt += 1
    if cnt > n - 1:
      break
print(round(dist,2))