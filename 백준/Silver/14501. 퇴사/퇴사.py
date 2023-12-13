import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N+1)
for i in range(N):
  for j in range(i+times[i][0], N+1):
    if dp[j] < dp[i]+times[i][1]:
      dp[j] = dp[i]+times[i][1]
print(dp[N])
