import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
arr = []
sum = []
for _ in range(N):
  arr.append(int(input()))
arr = sorted(arr)
for i in range(N):
  sum.append(arr[i]*(N-i))

print(max(arr+sum))