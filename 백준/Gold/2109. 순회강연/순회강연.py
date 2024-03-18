import sys
input = sys.stdin.readline

n = int(input())
cost = []
for _ in range(n):
  p, d = map(int,input().split())
  cost.append((p,d))

cost = sorted(cost, key=lambda x : (x[1],-x[0]))
answer = 0
for i in range(n,0,-1):
  li = []
  for p, d in cost:
    if d >= i:
      li.append((p,d))
  li = sorted(li, key=lambda x : -x[0])
  if li:
    answer += li[0][0]
    cost.remove(li[0])
print(answer)