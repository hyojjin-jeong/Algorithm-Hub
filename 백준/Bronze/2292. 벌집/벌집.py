import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
i = 1
Sum = 1
while True:
  if N == 1:
    print(1)
    break
  Sum += i*6
  i += 1
  if N <= Sum:
    print(i)
    break