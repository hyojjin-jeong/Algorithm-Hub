import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

n, w, L = map(int, input().split())
trucks = list(map(int,input().split()))
bridge = [0] * w
time = 0
while bridge:
  time += 1
  bridge.pop(0)
  if trucks:
    if sum(bridge) + trucks[0] <= L:
      bridge.append(trucks.pop(0))
    else:
      bridge.append(0)
print(time)
