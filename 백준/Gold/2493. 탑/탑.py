import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
tops = list(map(int,input().split()))
ans = []
stack = []

for i in range(N):
  while stack:
    if stack[-1][1] > tops[i]:
      ans.append(stack[-1][0] + 1) 
      break
    else:
      stack.pop()
  if not stack:
    ans.append(0)
  stack.append([i, tops[i]])
print(*ans)
  