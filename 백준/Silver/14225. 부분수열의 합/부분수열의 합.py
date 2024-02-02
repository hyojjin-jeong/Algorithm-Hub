import sys
input = sys.stdin.readline
from itertools import combinations #조합 사용

N = int(input())
S = list(map(int,input().split()))
sums = set()
for i in range(1,N+1):
  li = combinations(S,i)
  for j in li:
    sums.add(sum(j))
ans = 1
while True:
  if ans not in sums:
    print(ans)
    break
  ans += 1