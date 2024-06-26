import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
for i in range(2,N+1):
  dp[1][i] = i
for i in range(2,K+1):
  for j in range(4,N+1):
    dp[i][j] = dp[i-1][j-2] + dp[i][j-1]

print(dp[K][N] % 1000000003)