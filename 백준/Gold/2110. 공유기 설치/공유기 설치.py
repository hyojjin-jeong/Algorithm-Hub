import sys
input = sys.stdin.readline  #필수로 해놓기

N, C = map(int,input().split())

homes = [int(input()) for _ in range(N)]
homes.sort()
start, end = 1, homes[-1] - homes[0]
ans = 0

while start <= end:
  mid = (start + end) // 2
  current = homes[0]
  count = 1
  for i in range(1,len(homes)):
    if homes[i] >= current + mid:
      count += 1
      current = homes[i]
  if count >= C:
    start = mid + 1
    ans = mid
  else:
    end = mid - 1
print(ans)