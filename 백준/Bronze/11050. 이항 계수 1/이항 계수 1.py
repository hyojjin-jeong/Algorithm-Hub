import sys
import math
input = sys.stdin.readline

N, K = map(int,input().split())
if 0 <= K <= N:
  answer = math.factorial(N) / (math.factorial(K) * math.factorial(N-K))
else:
  answer = 0

print(int(answer))