import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a,b):
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for _ in range(m):
  s, a, b = map(int,input().split())
  if s == 0 and a != b:
    union(a,b)
  elif s == 1:
    a = find(a)
    b = find(b)
    if a == b:
      print("YES")
    else:
      print("NO")