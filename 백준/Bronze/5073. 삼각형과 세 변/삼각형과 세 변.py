import sys
input = sys.stdin.readline  #필수로 해놓기

while True:
  a, b, c = map(int,input().split())
  list = [a, b, c]
  Max = max(list)
  list.remove(Max)
  if a == 0 and b == 0 and c == 0:
    break
  elif Max >= sum(list):
    print("Invalid")
    continue
  if a == b and b == c:
    print("Equilateral")
    continue
  elif a == b or b == c or a == c:
    print("Isosceles")
    continue
  else:
    print("Scalene")