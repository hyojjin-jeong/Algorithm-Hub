import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nope = []
for _ in range(M):
  n = int(input())
  nope.append(n)
nope.append(N+1)
dp = [1] * (N+1)
if N >= 2:
  dp[2] = 2

for i in range(3,N+1):
  dp[i] = dp[i-1] + dp[i-2]
start = 1
ans = 1
for num in nope:
  ans *= dp[num - start]
  start = num + 1

print(ans)