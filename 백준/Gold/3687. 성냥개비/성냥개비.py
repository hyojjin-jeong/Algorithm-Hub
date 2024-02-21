import sys
input = sys.stdin.readline

T = int(input())
INF = float("inf")
dp = [INF] * 101
dp[2],dp[3],dp[4],dp[5],dp[6],dp[7] = 1,7,4,2,0,8

def min_num(x):
  if x <= 1:
    return dp[x]
  if dp[x] != INF:
    if x == 6:
      return 6
    return dp[x]
  else:
    for i in range(2,8):
      tmp = min_num(x-i)
      dp[x] = min(dp[x], tmp*10 + dp[i])
  return dp[x]

for _ in range(T):
  n = int(input())
  Min = min_num(n)
  if n % 2 == 0:
    Max = int("1" * (n//2))
  else:
    Max = int("7" + ("1" * ((n//2)-1)))
  print(Min, Max)