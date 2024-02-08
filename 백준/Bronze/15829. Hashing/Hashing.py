import sys
input = sys.stdin.readline

L = int(input())
s = input().rstrip()
sum = 0
for i in range(L):
  num = ord(s[i]) - 96
  sum += num * (31**i)
print(sum % 1234567891)