import sys
input = sys.stdin.readline  #필수로 해놓기

N, K = map(int,input().split())
list = list(map(int,input().split()))
count = [0] * (max(list)+1)
left, right = 0,0
answer = 0

while right < N:
  if count[list[right]] < K:
    count[list[right]] += 1
    right += 1
  else:
    count[list[left]] -= 1
    left += 1
  answer = max(answer, right - left)
print(answer)
