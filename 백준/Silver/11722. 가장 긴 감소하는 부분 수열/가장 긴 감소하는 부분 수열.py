import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1 for _ in range(N)]
for i in range(1,N):
  p = 0
  for j in range(i-1,-1,-1):
    if A[i] < A[j]:
      p = max(dp[j] + 1,p)
  dp[i] = max(dp[i],p)
print(max(dp))