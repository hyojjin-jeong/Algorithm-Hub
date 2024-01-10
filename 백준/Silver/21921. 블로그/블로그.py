import sys
input = sys.stdin.readline  #필수로 해놓기

N, X = map(int,input().split())
nums = list(map(int,input().split()))
left, right = 0, 0
ans = 0
m, s = 0, 0
while right < N:
  if right-left < X:
    s += nums[right]
    right += 1
  elif right-left == X:
    s -= nums[left]
    left += 1
  if s > m:
    ans = 0
    m = s
    ans += 1
  elif s == m:
    ans += 1

if m == 0:
  print("SAD")
else:
  print(m)
  print(ans)