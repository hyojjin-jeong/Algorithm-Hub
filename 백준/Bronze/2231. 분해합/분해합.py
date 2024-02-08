import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for i in range(1,N):
  sum = i
  s = str(i)
  for j in s:
    sum += int(j)
  if sum == N:
    answer = i
    break
print(answer)