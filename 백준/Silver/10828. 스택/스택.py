import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
  s = list(input().rstrip().split())
  if s[0] == "push":
    li.append(int(s[1]))
  elif s[0] == "pop":
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
  elif s[0] == "top":
    if li:
      print(li[-1])
    else:
      print(-1)