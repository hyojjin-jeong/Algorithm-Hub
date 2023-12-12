from re import M
import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

A = int(input())
arr = list(map(int,input().rsplit()))
dp = [0]*1005
dp[0] = arr[0]
for i in range(1, A):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j]+arr[i])
    else:
      dp[i] = max(dp[i],arr[i])
print(max(dp))
   