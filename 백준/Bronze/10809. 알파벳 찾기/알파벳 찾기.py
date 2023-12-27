import sys
input = sys.stdin.readline  #필수로 해놓기

S = input().rstrip()
alpha = [chr(code) for code in range(97,123)]
ans = []
for i in alpha:
  if S.count(i) != 0:
    ans.append(S.index(i))
  else:
    ans.append(-1)
print(*ans)