import sys

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
arr = list(map(int,input().split()))
dp = []
dp.append([])
dp.append([arr[0]])
for i in range(2,N+1):
  li = 0
  for j in range(1,i):
    if arr[i-1] > arr[j-1] and len(dp[li]) < len(dp[j]):
      li = j
  dp.append(dp[li] + [arr[i-1]])

ans = 0
count = 0
for i in range(len(dp)):
  if ans < len(dp[i]):
    ans = len(dp[i])
    count = i

print(ans)
print(*dp[count])
  