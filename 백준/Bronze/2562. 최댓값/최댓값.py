import sys
input = sys.stdin.readline  #필수로 해놓기

list = [ int(input()) for _ in range(9)]

M = max(list)
print(M)
print(list.index(M)+1)
