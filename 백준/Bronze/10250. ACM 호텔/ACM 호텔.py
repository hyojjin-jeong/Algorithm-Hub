import sys
input = sys.stdin.readline  #필수로 해놓기

T = int(input())
for _ in range(T):
  H,W,N = map(int,input().split())
  stair = N % H
  if stair == 0:
    stair = H
    rooms = N // H
  else:
    rooms = N // H + 1
  if rooms < 10:
    print(str(stair) + "0" + str(rooms))
  else:
    print(str(stair) + str(rooms))