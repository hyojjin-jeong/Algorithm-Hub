import sys
input = sys.stdin.readline  #필수로 해놓기
from math import ceil

T = int(input())
for _ in range(T):
  x, y = map(int,input().split())
  dist = y - x
  count = 0
  move_dist = 1
  max_count = 0
  while max_count < dist:
    count += 1
    max_count += move_dist
    if count % 2 == 0:
      move_dist += 1
  print(count)