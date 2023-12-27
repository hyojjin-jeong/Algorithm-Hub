import sys
input = sys.stdin.readline  #필수로 해놓기

A = int(input())
B = int(input())
C = int(input())
sum = A*B*C
list = list(str(sum))
for i in range(10):
  print(list.count(str(i)))