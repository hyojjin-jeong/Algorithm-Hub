import sys
input = sys.stdin.readline  #필수로 해놓기
import math #수학 사용

H, W, N, M = map(int,input().split())
a = math.ceil(H/(N+1))
b = math.ceil(W/(M+1))
print(a*b)