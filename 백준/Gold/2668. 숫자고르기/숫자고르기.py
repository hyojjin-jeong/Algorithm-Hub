import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
graphs = [[] for _ in range(N+1)]
for i in range(N):
  num = int(input())
  graphs[i+1].append(num)

def dfs(start):
  for node in graphs[start]:
    if not visited[node]:
      visited[node] = True
      tmpUp.add(start)
      tmpDown.add(node)
      if tmpUp == tmpDown:
        ans.extend(list(tmpDown))
        return
      dfs(node)
ans = []
for i in range(1,N+1):
  visited = [False for _ in range(N+1)]
  tmpUp = set()
  tmpDown = set()
  dfs(i)
ans = list(set(ans))
ans.sort()
print(len(ans))
for i in ans:
  print(i)