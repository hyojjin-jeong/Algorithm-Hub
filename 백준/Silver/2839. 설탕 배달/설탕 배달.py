import sys
input = sys.stdin.readline

N = int(input())
INF = float("inf")
dp = [INF] * (5001)
dp[0] = 0
dp[3] = 1
dp[5] = 1
for i in range(6,N+1):
  dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)

if dp[N] == INF:
  print(-1)
else:
  print(dp[N])