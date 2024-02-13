import sys
import math
input = sys.stdin.readline

N = int(input())
fact = str(math.factorial(N))
answer = 0
for i in range(len(fact)-1,-1,-1):
  if fact[i] == '0':
    answer += 1
  else:
    break

print(answer)