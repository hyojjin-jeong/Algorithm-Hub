import sys
input = sys.stdin.readline  #필수로 해놓기

N = int(input())
alpha = {chr(i+ord('A')):[] for i in range(10)}
weight = [0] * 10
first = []
li = []
for _ in range(N):
  li.append(input().rstrip())

for word in li:
  for j in range(len(word)):
    weight[ord(word[j]) - ord('A')] += 10**(len(word) - j - 1)
  first.append(word[0])
for i in range(len(weight)):
  alpha[chr(i+ord('A'))].append(weight[i])

alpha = sorted(alpha.items(), key=lambda x: x[1], reverse = True)

for i in range(9, -1, -1):
  if alpha[i][0] not in first:
    temp = alpha[i]
    alpha.remove(temp)
    alpha.append(temp)
    break

result = 0
for i in range(10):
  result += int(alpha[i][1][0]) * (9-i)
print(result)