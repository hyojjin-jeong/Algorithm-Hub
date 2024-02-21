import sys
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
input = sys.stdin.readline

n, m = map(int,input().split())
name = [int(input()) for _ in range(n)]
INF = float("inf")
dp = [INF] * (n+1)
dp[n] = 0

def note(index):
  if dp[index] < INF:
    return dp[index]
  remain = m - name[index]
  for i in range(index+1, n+1):
    if remain >= 0:
      if i == n:
        dp[index] = 0
        break
      dp[index] = min(dp[index], remain * remain + note(i))
      remain -= name[i] + 1
  return dp[index]

print(note(0))