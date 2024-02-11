import sys
input = sys.stdin.readline

N, M = map(int,input().split())
memory = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
lenth = sum(cost) + 1
dp = [[0 for _ in range(lenth)] for _ in range(N+1)]
answer = sum(cost)
for i in range(1,N+1):
  byte = memory[i]
  c = cost[i]
  for j in range(lenth):
    dp[i][j] = dp[i-1][j]
  for j in range(c,lenth):
    dp[i][j] = max(dp[i-1][j-c] + byte, dp[i][j])
    if dp[i][j] >= M:
      answer = min(answer, j)

print(answer)