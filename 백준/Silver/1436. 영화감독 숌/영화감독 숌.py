import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
num = 666
cnt = 1
while cnt < N:
  num += 1
  if "666" in str(num):
    cnt += 1
print(num)
