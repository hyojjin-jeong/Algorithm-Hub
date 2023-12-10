import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

T = int(input())
dp = [-1] * 45
dp[0] = 0
dp[1] = 1
count = [[0,0]]*45
count[0] = [1,0]
count[1] = [0,1]
def fibo(x):
  global c0,c1
  if x == 0:
    c0 += 1
  elif x == 1:
    c1 += 1
  if dp[x] == -1:
    dp[x] = fibo(x-2) + fibo(x-1)
    count[x] = [count[x-2][0]+count[x-1][0],count[x-2][1]+count[x-1][1]]
    
  return dp[x]
ans = []
for _ in range(T):
  N = int(input())
  c0,c1=0,0
  fibo(N)
  ans.append(count[N])

for i in range(T):
  print(*ans[i])