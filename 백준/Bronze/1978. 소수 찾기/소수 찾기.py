import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
answer = 0
for n in nums:
  cnt = 0
  if n == 1:
    continue
  for i in range(1, n):
    if n % i == 0:
      cnt += 1
  if cnt == 1:
    answer += 1
print(answer)