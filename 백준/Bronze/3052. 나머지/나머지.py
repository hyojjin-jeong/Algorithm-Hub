import sys
input = sys.stdin.readline  #필수로 해놓기

numbers = [int(input()) for _ in range(10)]

ans = set()
for num in numbers:
  ans.add(num%42)
print(len(ans))