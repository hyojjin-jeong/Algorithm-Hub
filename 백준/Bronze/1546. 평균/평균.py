import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int,input().split()))

max_s = max(score)
sum = 0
for s in score:
  sum += (s/max_s) * 100
print(sum / len(score))