import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
numbers = input().rstrip()
sum = 0
for num in numbers:
  sum += int(num)
print(sum)

