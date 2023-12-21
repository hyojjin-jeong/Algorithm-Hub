import sys
input = sys.stdin.readline  #필수로 해놓기

word = input().rstrip()
word = sorted(word.upper())
alpha = list(set(word))
ans = []
for a in alpha:
  ans.append(word.count(a))
Max = max(ans)
index = ans.index(Max)
if ans.count(Max) > 1:
  print("?")
else:
  print(alpha[index])