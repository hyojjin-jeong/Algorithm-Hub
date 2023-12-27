import sys
input = sys.stdin.readline  #필수로 해놓기

list = list(map(int,input().split()))
sum = 0
for num in list:
  sum += num*num
print(sum%10)