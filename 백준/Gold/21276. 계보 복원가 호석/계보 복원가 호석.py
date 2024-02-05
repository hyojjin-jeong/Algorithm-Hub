import sys
input = sys.stdin.readline
from collections import defaultdict, deque

N = int(input())
names = list(input().split())
names.sort()
parent = {i: [] for i in names}
child = {i: [] for i in names}
indegree = defaultdict(int)
answer = defaultdict(list)
M = int(input())
for _ in range(M):
  x, y = input().split()
  child[x].append(y)
  parent[y].append(x)
  indegree[x] += 1
root = []
for key, value in child.items():
  if len(value) == 0:
    root.append(key)
root.sort()
print(len(root))
print(*root)

def findchild(root):
  q = deque([root])

  while q:
    p = q.popleft()
    for c in parent[p]:
      indegree[c] -= 1
      if indegree[c] == 0:
        answer[p].append(c)
        q.append(c)
for r in root:
  findchild(r)
for p in names:
  print(p,len(answer[p]), *sorted(answer[p]))