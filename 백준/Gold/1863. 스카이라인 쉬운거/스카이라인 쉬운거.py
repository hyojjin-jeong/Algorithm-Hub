import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요

n = int(input())
build = []
ans = 0
for _ in range(n):
  x, y = map(int,input().split())
  while len(build) > 0 and build[-1] > y:
    ans += 1
    build.pop()
  if len(build) > 0 and build[-1] == y:
    continue
  build.append(y)
while len(build) > 0:
  if build[-1] > 0:
    ans += 1
  build.pop()
print(ans)
    