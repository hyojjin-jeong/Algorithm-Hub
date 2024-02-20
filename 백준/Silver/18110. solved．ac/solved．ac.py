import sys
input = sys.stdin.readline

n = int(input())
level = [int(input()) for _ in range(n)]
def half(num):
  so = num - int(num)
  if so >= 0.5:
    return int(num) + 1
  else:
    return int(num)
if n == 0:
  print(0)
else:
  level.sort()
  nope = half(n * 0.15)
  if nope == 0:
    total_level = level[:]
  else:
    total_level = level[nope:-nope]
  print(half(sum(total_level) / len(total_level)))