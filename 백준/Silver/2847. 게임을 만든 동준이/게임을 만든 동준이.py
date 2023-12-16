import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
scores = []
for _ in range(N):
  scores.append(int(input()))
next = scores[N-1]
ans = 0
for i in range(N-2,-1,-1):
  if scores[i] >= next:
    ans += scores[i] - (next-1)
    scores[i] = next - 1
  next = scores[i]
print(ans)