import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))
answer = 0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if answer < nums[i] + nums[j] + nums[k] <= M:
        answer = nums[i] + nums[j] + nums[k]
print(answer)