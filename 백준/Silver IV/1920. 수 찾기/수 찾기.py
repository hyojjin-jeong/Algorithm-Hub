import sys
import math
input = sys.stdin.readline

N = int(input())
A = set(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))

for n in nums:
  if n in A:
    print(1)
  else:
    print(0)