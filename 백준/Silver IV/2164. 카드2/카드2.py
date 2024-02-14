import sys
from collections import deque  #큐 사용
input = sys.stdin.readline

N = int(input())
li = deque([i for i in range(1,N+1)])
while (len(li) > 1):
  li.popleft()
  change = li.popleft()
  li.append(change)
print(li[0])