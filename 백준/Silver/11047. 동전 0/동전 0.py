import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N, K = map(int,input().split())
coins = []
for _ in range(N):
  coins.append(int(input()))
coins = sorted(coins, reverse = True)
cnt = 0
for i in range(N):
  if coins[i] <= K:
    cnt += K // coins[i]
    K -= (K // coins[i])*coins[i]
print(cnt)