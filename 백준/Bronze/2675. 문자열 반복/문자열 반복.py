import sys
input = sys.stdin.readline  #필수로 해놓기

T = int(input())
for _ in range(T):
  R, S = input().split()
  R = int(R)
  ans = ""
  for s in S:
    ans += s*R
  print(ans)