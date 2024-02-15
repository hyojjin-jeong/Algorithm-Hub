import sys
input = sys.stdin.readline

n, k = map(int,input().split())
INF = float("inf")
much = [0]
for _ in range(n):
  m = int(input())
  much.append(m)

much.sort()
dp = [INF] * (k+1)
dp[0] = 0

for c in much:
  for i in range(c,k+1):
    if dp[i] > 0:
      dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == INF:
  print(-1)

else:
  print(dp[k])