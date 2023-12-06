import sys

input = sys.stdin.readline #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

F,S,G,U,D = map(int,input().split())
visited = [-1]*(F+1)
def bfs(start):
  queue = deque([start])
  visited[start] = 0
  while queue:
    x = queue.popleft()
    if x == G:
      return visited[x]
    n = visited[x]
    nx = [x+U,x-D]
    for i in range(len(nx)):
      if (1 <= nx[i] <= F) and visited[nx[i]] == -1:
        visited[nx[i]] = n+1
        queue.append(nx[i])
  return -1

answer = bfs(S)

if answer == -1:
  print("use the stairs")
else:
  print(answer)