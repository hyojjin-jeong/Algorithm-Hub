import sys
input = sys.stdin.readline  #필수로 해놓기
sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용

n = int(input())
x, y = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  i, j = map(int,input().split())
  graph[i].append(j)
  graph[j].append(i)

visited = [False] * (n+1)
ans = -1
def dfs(x, cnt):
  global ans
  visited[x] = True
  for node in graph[x]:
    if node == y:
      ans = cnt
      return cnt
    if not visited[node]:
      dfs(node,cnt+1)
  
dfs(x,1)
print(ans)