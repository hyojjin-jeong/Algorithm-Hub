import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

T = int(input())
dp = [0] * 102
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5

def fibo(x):
  if dp[x] == 0:
    dp[x] = fibo(x-5) + fibo(x-1)
    
  return dp[x]
ans = []
for _ in range(T):
  N = int(input())
  ans.append(fibo(N))
for i in range(len(ans)):
  print(ans[i])