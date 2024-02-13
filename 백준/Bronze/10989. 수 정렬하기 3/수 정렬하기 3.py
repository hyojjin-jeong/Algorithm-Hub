import sys
input = sys.stdin.readline

N = int(input())
answer = {i: 0 for i in range(1,10001)}
for _ in range(N):
  num = int(input())
  answer[num] += 1

for key, value in answer.items():
  for _ in range(value):
    print(key)
