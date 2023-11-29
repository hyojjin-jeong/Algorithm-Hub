import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1,node2 = map(int,input().split())
    graph[node2].append(node1)

X = int(input())

visited = [False] * (N+1)
answer = 0

def dfs(node):
  global answer
  visited[node] = True
  for i in graph[node]:
    if not visited[i]:
        answer += 1
        dfs(i)

dfs(X)
  
print(answer)