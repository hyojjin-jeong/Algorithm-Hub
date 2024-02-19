import sys
from collections import deque  #큐 사용
input = sys.stdin.readline

N = int(input())
li = deque()
for _ in range(N):
  s = list(input().rstrip().split())
  if s[0] == "push_front":
    li.appendleft(int(s[1]))
  elif s[0] == "push_back":
    li.append(int(s[1]))
  elif s[0] == "pop_front":
    if li:
      print(li.popleft())
    else:
      print(-1)
  elif s[0] == "pop_back":
    if li:
      print(li.pop())
    else:
      print(-1)
  elif s[0] == "size":
    print(len(li))
  elif s[0] == "empty":
    if li:
      print(0)
    else:
      print(1)
  elif s[0] == "front":
    if li:
      print(li[0])
    else:
      print(-1)
  elif s[0] == "back":
    if li:
      print(li[-1])
    else:
      print(-1)