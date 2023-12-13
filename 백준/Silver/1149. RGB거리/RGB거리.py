import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
houses = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0][0] = houses[0][0]
dp[0][1] = houses[0][1]
dp[0][2] = houses[0][2]

for i in range(1,N):
  dp[i][0] = min(dp[i-1][1]+houses[i][0], dp[i-1][2]+houses[i][0])
  dp[i][1] = min(dp[i-1][0]+houses[i][1], dp[i-1][2]+houses[i][1])
  dp[i][2] = min(dp[i-1][0]+houses[i][2], dp[i-1][1]+houses[i][2])
print(min(dp[N-1]))