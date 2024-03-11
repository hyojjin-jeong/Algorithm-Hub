from sys import stdin
input = stdin.readline

N = int(input())
a = [False, False] + [True] * (N-1)
sosu = []
for i in range(2, N+1):
  if a[i]:
    sosu.append(i)
    for j in range(2*i, N+1, i):
      a[j] = False
left, right = 0, 0
answer = 0
if sosu:
  sum = sosu[0]
  while left < len(sosu) and sosu:
    if N > sum:
      if right != len(sosu) - 1:
        right += 1
        sum += sosu[right]
      else:
        sum -= sosu[left]
        left += 1
    else:
      if N == sum:
        answer += 1
      sum -= sosu[left]
      left += 1
print(answer)