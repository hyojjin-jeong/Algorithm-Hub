import sys
input = sys.stdin.readline  #필수로 해놓기
import math #수학 사용

N = int(input())
M = int(input())
lamps = list(map(int,input().split()))
height = lamps[0]
for i in range(M-1):
  h = math.ceil((lamps[i+1] - lamps[i]) / 2)
  if h > height:
    height = h
if N - lamps[-1] > height:
  height = N - lamps[-1]
print(height)