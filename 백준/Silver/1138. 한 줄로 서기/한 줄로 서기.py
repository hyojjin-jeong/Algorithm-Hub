import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
reports = list(map(int, input().split()))
ans = [0]*N
for i in range(N):
  index = 0
  for j in range(N):
    if index == reports[i] and ans[j] == 0:
      ans[j] = i+1
      break
    if ans[j] == 0:
      index += 1
print(*ans)
              
