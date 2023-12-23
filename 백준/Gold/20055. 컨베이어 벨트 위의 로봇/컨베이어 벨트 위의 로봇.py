import sys
input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

N, K = map(int,input().split())
cnts = deque(list(map(int,input().split())))
robots = deque([0] * N)
ans = 0

while cnts.count(0) < K:
  cnts.rotate(1)
  robots.rotate(1)
  robots[-1] = 0
  for i in range(N-2,-1,-1):
    if robots[i] == 1 and robots[i+1] == 0 and cnts[i+1] >= 1:
        robots[i+1] = 1
        robots[i] = 0
        cnts[i+1] -= 1
    robots[-1] = 0
  if cnts[0] > 0 and robots[0] == 0:
    cnts[0] -= 1
    robots[0] = 1
  ans += 1
print(ans)
