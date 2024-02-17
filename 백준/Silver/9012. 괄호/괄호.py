import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  str = input().rstrip()
  stack = []
  nope = 0
  for s in str:
    if s == "(":
      stack.append(s)
    elif s == ")":
      if stack:
        stack.pop()
      else:
        nope = 1
        break
  if nope == 0 and len(stack) == 0:
    print("YES")
  else:
    print("NO")