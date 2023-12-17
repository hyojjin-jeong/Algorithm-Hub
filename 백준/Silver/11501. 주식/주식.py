import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

T = int(input())
ans = []
for _ in range(T):
  N = int(input())
  nums = list(map(int,input().split()))
  ans = 0
  Max = nums[-1]
  for i in range(N-2,-1,-1):
    if Max > nums[i]:
      ans += Max - nums[i]
    else:
      Max = nums[i]
  print(ans)