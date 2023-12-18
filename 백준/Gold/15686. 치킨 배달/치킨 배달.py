import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용
from itertools import combinations #조합 사용

N, M = map(int,input().split())
cities = [list(map(int,input().split())) for _ in range(N)]
chickens = []
homes = []
for i in range(N):
  for j in range(N):
    if cities[i][j] == 1:
      homes.append([i+1,j+1])
    elif cities[i][j] == 2:
      chickens.append([i+1,j+1])
combi = list(combinations(chickens, M))
ans = []
for com in combi:
  s = 0
  for x,y in homes:
    mini = []
    for a,b in com:
      mini.append(abs(x-a)+abs(y-b))
    s += min(mini)
  ans.append(s)
print(min(ans))