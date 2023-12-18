import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
current = list(map(int,input().rstrip()))
wanted = list(map(int,input().rstrip()))

def change(a,B):
  A = a[:]
  touch = 0
  for i in range(1,N):
    if A[i-1] == B[i-1]:
      continue
    touch += 1
    for j in range(i-1,i+2):
      if j < N:
        A[j] = 1 - A[j]
  if A == B:
    return touch
  else:
    return float("inf")

second = change(current, wanted)

current[0] = 1 - current[0]
current[1] = 1 - current[1]

first = change(current, wanted) + 1
ans = min(first,second)
if ans == float("inf"):
  print(-1)
else:
  print(ans)
