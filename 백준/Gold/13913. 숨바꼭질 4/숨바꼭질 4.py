import sys
from typing import Counter

input = sys.stdin.readline  #필수로 해놓기
#sys.setrecursionlimit(10**7) #재귀함수 사용 시 필요
from collections import deque  #큐 사용

N,K = map(int,input().split())
visited = [0] * 100001
parents = [0] * 100001

def bfs():
  queue = deque([N])
  while queue:
    x = queue.popleft()
    if x == K:
      return 0
    moves=[x+1,x-1,2*x]
    for i in moves:
      if (0 <= i <= 100000) and visited[i] == 0:
        visited[i] = visited[x] + 1
        queue.append(i)
        parents[i] = x

answer = bfs()
print(visited[K])

ans = [N] * (visited[K]+1)
n = K
for i in range(visited[K],0,-1):
  ans[i] = n
  n = parents[n]
print(*ans)
