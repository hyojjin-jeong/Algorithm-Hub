import sys

input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

A,K = map(int,input().split())

answer = 0
while True:
  if K == A:
    break
  if K % 2 != 0:
    K -= 1
    answer += 1
  else:
    if int(K/2) >= A:
      K = int(K/2)
      answer += 1
    else:
      K -= 1
      answer += 1
  

print(answer)