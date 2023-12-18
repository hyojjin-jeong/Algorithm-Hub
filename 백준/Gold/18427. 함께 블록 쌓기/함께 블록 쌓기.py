import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용
#from itertools import combinations #조합 사용

N, M, H = map(int,input().split())
students = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (H+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
  dp[i] = dp[i-1].copy()
  for j in students[i-1]:
    for k in range(j, H+1):
      dp[i][k] += dp[i-1][k-j]
print(dp[N][H]%10007)
