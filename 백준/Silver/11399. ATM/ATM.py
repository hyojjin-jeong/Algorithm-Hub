import sys

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

N = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
sum = 0
for i in range(len(arr)):
  sum += (N-i)*arr[i]

print(sum)

