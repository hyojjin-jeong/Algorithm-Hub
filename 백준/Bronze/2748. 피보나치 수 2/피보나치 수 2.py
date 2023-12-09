import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

n = int(input())
dp = [0]*(n+2)
dp[0] = 1
dp[1] = 1
dp[2] = 1

def fibo(x):
  if dp[x] == 0:
    dp[x] = fibo(x-2)+fibo(x-1)
  
  return dp[x]

print(fibo(n))