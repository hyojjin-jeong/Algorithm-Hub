import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

n, m = map(int,input().split())
nums = list(map(int,input().split()))

for _ in range(m):
  nums = sorted(nums)
  s = nums[0]+nums[1]
  nums[0] = s
  nums[1] = s
print(sum(nums))