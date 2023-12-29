import sys
input = sys.stdin.readline  #필수로 해놓기

N, M = map(int,input().split())
words = {}
for _ in range(N):
  word = input().rstrip()
  if len(word) >= M:
    if word in words:
      words[word] += 1
    else:
      words[word] = 1
words = sorted(words.items(), key=lambda x : (-x[1],-len(x[0]),x[0]))
for i in words:
  print(i[0])