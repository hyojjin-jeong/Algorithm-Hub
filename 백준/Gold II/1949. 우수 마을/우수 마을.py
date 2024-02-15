import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
town = [0] + list(map(int,input().split()))

graph = {i: [] for i in range(1,N+1)}
for _ in range(N-1):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(start):
  visited[start] = True
  for neigh in graph[start]:
    if not visited[neigh]:
      dfs(neigh)
      dp[start][1] += dp[neigh][0]
      dp[start][0] += max(dp[neigh][0], dp[neigh][1])

visited = [False for _ in range(N+1)]
dp = [[0, town[i]] * 2 for i in range(N+1)]

dfs(1)
print(max(dp[1][1],dp[1][0]))