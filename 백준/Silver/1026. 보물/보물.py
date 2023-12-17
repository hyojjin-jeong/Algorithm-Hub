import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
B = list(map(int, input().split()))
B = sorted(B, reverse=True)
ans = 0
for i in range(N):
  ans += A[i] * B[i]
print(ans)