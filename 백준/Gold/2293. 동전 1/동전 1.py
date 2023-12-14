import sys

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
for i in range(n):
  for j in range(k+1):
    if coins[i] > j:
      continue
    elif coins[i] == j:
      dp[j] += 1
    else:
      dp[j] += dp[j - coins[i]]
print(dp[-1])
  