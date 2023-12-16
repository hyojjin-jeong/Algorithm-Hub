import sys

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

S = input().rstrip()
c1, c0 = 0, 0
temp = S[0]
if temp == "1":
  c1 += 1
else:
  c0 += 1
for i in range(1,len(S)):
  if S[i] != temp:
    if S[i] =="1":
      c1 += 1
    else:
      c0 += 1
  temp = S[i]
if c1 == 1 and c0 == 0:
  print(0)
elif c0 == 1 and c1 == 0:
  print(0)
else:
  print(min(c1,c0))