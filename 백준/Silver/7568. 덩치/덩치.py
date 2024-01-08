import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
peoples = [list(map(int,input().split())) for _ in range(N)]
ans = []

for p in peoples:
  cnt = 0
  for i in peoples:
    if p[0] < i[0] and p[1] < i[1]:
      cnt += 1
  ans.append(cnt+1)
print(*ans)