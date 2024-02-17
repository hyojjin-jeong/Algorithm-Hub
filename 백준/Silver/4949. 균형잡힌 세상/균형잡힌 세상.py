import sys
input = sys.stdin.readline

while True:
  s = input().rstrip()
  if s == ".":
    break
  stack = []
  nope = 0
  for i in s:
    if i == "(" or i == "[":
      stack.append(i)
    elif i == "]":
      if len(stack) == 0:
        nope = 1
        break
      if stack[-1] == "[":
        stack.pop()
      else:
        nope = 1
        break
    elif i == ")":
      if len(stack) == 0:
        nope = 1
        break
      if stack[-1] == "(":
        stack.pop()
      else:
        nope = 1
        break
  if nope == 0 and len(stack) == 0:
    print("yes")
  else:
    print("no")