import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
dp = [0]*(N+2)
dp[1] = 1
dp[2] = 1
for i in range(3,N+1):
  dp[i] = dp[i-1]+dp[i-2]

print(dp[N])
