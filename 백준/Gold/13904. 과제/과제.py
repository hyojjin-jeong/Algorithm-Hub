from sys import stdin
input = stdin.readline
from collections import defaultdict #dict 초기화

N = int(input())
works = [[] for _ in range(1001)]
max_day = 0
for _ in range(N):
  d, w = map(int,input().split())
  max_day = max(max_day, d)
  works[d].append(w)
answer = 0
for i in range(max_day,0,-1):
  d = 0
  max_s = 0
  for j in range(i,max_day+1):
    if works[j]:
      max_j = max(works[j])
    else:
      max_j = 0
    if max_s < max_j:
      d = j
      max_s = max_j
  if d != 0:
    works[d].remove(max_s)
    answer += max_s
print(answer)