import sys
input = sys.stdin.readline

N, K = map(int,input().split())
answer = []
li = [i for i in range(1,N+1)]
index = 0
while li:
  index += K - 1
  if index >= len(li):
    index %= len(li)
  answer.append(str(li.pop(index)))

print("<", ", ".join(answer), ">", sep="")