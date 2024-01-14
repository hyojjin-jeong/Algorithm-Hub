import sys
input = sys.stdin.readline  #필수로 해놓기

N, K, P, X = map(int,input().split())
led = [[] for _ in range(10)]
led[0] = [0,4,3,3,4,3,2,3,1,2]
led[1] = [4,0,5,3,2,5,6,1,5,4]
led[2] = [3,5,0,2,5,4,3,4,2,3]
led[3] = [3,3,2,0,3,2,3,2,2,1]
led[4] = [4,2,5,3,0,3,4,3,3,2]
led[5] = [3,5,4,2,3,0,1,4,2,1]
led[6] = [2,6,3,3,4,1,0,5,1,2]
led[7] = [3,1,4,2,3,4,5,0,4,3]
led[8] = [1,5,2,2,3,2,1,4,0,1]
led[9] = [2,4,3,1,2,1,2,3,1,0]
X = str(X)
while K != len(X):
  X = '0' + X
X = list(X)
ans = 0
for i in range(1,N+1):
  str_i = str(i)
  while K != len(str_i):
    str_i = '0' + str_i
  li_i = list(str_i)
  s = 0
  for j in range(K):
    s += led[int(X[j])][int(li_i[j])]
  if 0 < s <= P:
    ans += 1
print(ans)