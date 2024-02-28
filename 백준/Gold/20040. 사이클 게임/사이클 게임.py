from sys import stdin
input = stdin.readline

n, m = map(int,input().split())
li = [i for i in range(n)]

def find(x):
  if li[x] != x:
    return find(li[x])
  return x

def union(a,b):
  a = find(a)
  b = find(b)
  if a < b:
    li[b] = a
  elif a > b:
    li[a] = b
  else:
    return True
  return False

cnt = 0
for i in range(1,m+1):
  c, d = map(int,input().split())
  if union(c,d):
    print(i)
    break
  else:
    cnt += 1

if cnt == m:
  print(0)