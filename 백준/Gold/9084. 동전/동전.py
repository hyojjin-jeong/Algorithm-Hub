from re import M
import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

T = int(input())
ans = []
for _ in range(T):
  N = int(input())
  coins = list(map(int,input().split()))
  M = int(input())
  dp = [0]*(M+1)
  dp[0] = 1
  for coin in coins:
    for i in range(1, M+1):
      if i >= coin:
        dp[i] += dp[i-coin]
  ans.append(dp[M])
for a in ans:
  print(a)
  
  