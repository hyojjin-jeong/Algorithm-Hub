import sys
input = sys.stdin.readline  #필수로 해놓기
from collections import deque  #큐 사용

N, d, k, c = map(int,input().split())
list = [int(input()) for _ in range(N)]
list = list + list
left, right = 0, k
answer = 0
while left < N:
  eat = set(list[left:right])
  eat.add(c)
  left += 1
  right += 1
  answer = max(answer, len(eat))
print(answer)