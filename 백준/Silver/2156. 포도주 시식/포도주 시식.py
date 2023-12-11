import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
dp = [-1] * 10002
wines = [int(input()) for _ in range(N)]
wines = [0] + wines
dp[0] = 0
dp[1] = wines[1]
if N >= 2:
  dp[2] = wines[1] + wines[2]


for x in range(3,N+1):
  dp[x] = max(wines[x]+wines[x-1]+dp[x-3],wines[x]+dp[x-2],dp[x-1])


print(dp[N])