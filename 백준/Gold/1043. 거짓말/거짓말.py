import sys
input = sys.stdin.readline  #필수로 해놓기
from math import ceil #올림 함수

N, M = map(int,input().split())
t = list(map(int,input().split()))
n = t[0]
trues = set(t[1:n+1])
answer = 0
parties = []
for _ in range(M):
  p = list(map(int,input().split()))
  n = p[0]
  parties.append(p[1:n+1])
while len(trues) != 0 and len(parties) != 0:
  t = set()
  p = []
  for i in range(len(parties)):
    cnt = 0
    for j in parties[i]:
      if j in trues:
        t.update(parties[i])
        cnt = 1
        break
    if cnt == 0:
      p.append(parties[i])
  trues = t
  parties = p
print(len(parties))
