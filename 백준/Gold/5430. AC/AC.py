import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  p = input().rstrip()
  n = int(input())
  s = input().rstrip()
  s = s[1:-1]
  err = 0
  if s:
    li = list(s.split(","))
  else:
    li = []
  r = 0
  for i in p:
    if i == "R":
      r += 1
    elif i == "D":
      if li:
        if r % 2 == 0:
          li.pop(0)
        else:
          li.pop()
      else:
        err = 1
        break
    else:
      err = 1
      break
  if err == 1:
    print("error")
  else:
    if r % 2 == 1:
      li.reverse()
    print("[", end="")
    answer = ','.join(li)
    print(answer, end="")
    print("]")