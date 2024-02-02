import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
ans = 0
for i in range(len(b)+1):
  for j in range(len(a)+1):
    if i == 0 or j == 0:
      dp[i][j] = 0
    elif b[i-1] == a[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
      ans = max(ans, dp[i][j])
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(ans)