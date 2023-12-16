import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = input().rstrip()
s = 0
num = []
mi = []
j = 0
for i in range(len(N)):
  if N[i] == '+':
    num.append(int(N[s:i]))
    s = i+1
  elif N[i] == '-':
    num.append(int(N[s:i]))
    s = i+1
    mi.append(sum(num))
    num = []
  elif i == len(N)-1:
    num.append(int(N[s:i+1]))
    mi.append(sum(num))

ans = mi[0]
for i in range(1,len(mi)):
  ans -= mi[i]
print(ans)