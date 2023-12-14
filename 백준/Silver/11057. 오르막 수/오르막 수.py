import sys

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())

dp = [[0] * 10 for _ in range(N)]
for i in range(10):
  dp[0][i] = 1
for i in range(1,N):
  dp[i][0] = 0
  
for i in range(1,N):
  for j in range(1,10):
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
ans = 0
for i in range(N):
  ans += sum(dp[i])
print(ans%10007)
