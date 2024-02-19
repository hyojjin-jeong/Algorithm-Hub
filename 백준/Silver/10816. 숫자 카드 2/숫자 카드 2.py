import sys
from collections import defaultdict #dict 초기화
input = sys.stdin.readline

N = int(input())
card = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))

num_dict = defaultdict(int)
for c in card:
  num_dict[c] += 1

for n in nums:
  print(num_dict[n], end=" ")