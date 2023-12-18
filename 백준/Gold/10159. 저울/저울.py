import sys
input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
#from collections import deque  #큐 사용
#from itertools import combinations #조합 사용

N = int(input())
M = int(input())
heavy = [[] for _ in range(N)]
light = [[] for _ in range(N)]
for _ in range(M):
  i, j = map(int,input().split())
  heavy[i-1].append(j-1)
  light[j-1].append(i-1)

def dfs(x,weights):
  global cnt
  for node in weights[x]:
    if not visited[node]:
      cnt += 1
      visited[node] = True
      dfs(node,weights)
for i in range(N):
  cnt = 0
  visited = [False]*N
  visited[i] = True
  dfs(i,heavy)
  visited = [False]*N
  visited[i] = True
  dfs(i,light)
  print(N-1-cnt)
  