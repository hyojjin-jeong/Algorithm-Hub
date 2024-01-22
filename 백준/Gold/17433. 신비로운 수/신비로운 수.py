import sys
input = sys.stdin.readline  #필수로 해놓기

T = int(input())
def gcd(a,b):
  while b != 0:
    a, b = b, a % b
  return a
for _ in range(T):
  N = int(input())
  nums = list(map(int,input().split()))
  nums.sort()
  diff = set()
  for i in range(1,N):
    diff.add(nums[i] - nums[i-1])
  diff = list(diff)
  if diff == [0]:
    print("INFINITY")
    continue
  start = diff[0]
  for j in range(1, len(diff)):
    start = gcd(start, diff[j])
  print(start)