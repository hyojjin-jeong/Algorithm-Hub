import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
A = list(map(int,input().split()))
A.sort()
answer = 0

for i in range(N):
  tmp = A[:i] + A[i+1:]
  left, right = 0, len(tmp) - 1
  while left < right:
    s = tmp[left] + tmp[right]
    if s == A[i]:
      answer += 1
      break
    if s < A[i]:
      left += 1
    else:
      right -= 1
print(answer)
