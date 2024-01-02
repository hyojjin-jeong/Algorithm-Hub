import sys
input = sys.stdin.readline  #필수로 해놓기

N, K = map(int,input().split())
S = list(input().rstrip())
ans = 0
for i in range(N):
  if S[i] == "P":
    for j in range(i-K,i+K+1):
      if 0 <= j < N and S[j] == "H":
        ans += 1
        S[j] = "E"
        break
print(ans)
        