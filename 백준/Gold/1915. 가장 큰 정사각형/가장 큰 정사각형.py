import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(input().rstrip()) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
  dp[i][0] = int(maps[i][0])
for i in range(m):
  dp[0][i] = int(maps[0][i])

max_len = max(dp[0])
for i in range(1,n):
  for j in range(1,m):
    if maps[i][j] == '1':
      dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
  max_len = max(max_len,max(dp[i]))
print(max_len * max_len)