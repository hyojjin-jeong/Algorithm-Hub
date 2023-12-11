import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
dp = [-1] * 1002
dp[0] = 0
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1
dp[5] = 1

for i in range(6,N+1):
  if dp[i-1] + dp[i-3] + dp[i-4] == 3:
      dp[i] = 0
  else:
      dp[i] = 1

if dp[N] == 0:
    print("CY")
else:
    print("SK")