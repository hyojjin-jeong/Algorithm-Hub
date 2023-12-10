import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

n = int(input())
stairs = [0]
for _ in range(n):
  a = int(input())
  stairs.append(a)
dp = [-1] * 305
dp[0] = 0
dp[1] = stairs[1]
if n > 1:
  dp[2] = stairs[1]+stairs[2]
def fibo(x):
  if dp[x] == -1:
    dp[x] = max(stairs[x]+stairs[x-1]+fibo(x-3),stairs[x]+fibo(x-2))
  return dp[x]

print(fibo(n))