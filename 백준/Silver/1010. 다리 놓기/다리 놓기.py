import sys
input = sys.stdin.readline  #필수로 해놓기
import math

T = int(input())
for _ in range(T):
  N, M = map(int,input().split())
  print(int(math.factorial(M) / (math.factorial(M-N) * math.factorial(N))))