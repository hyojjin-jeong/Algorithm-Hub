import sys
input = sys.stdin.readline  #필수로 해놓기
import math

N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
ans = []
for a in A:
  for i in range(len(B)):
    if a == B[i]:
      ans.append(i)
      B[i] = -1
      break
print(*ans)