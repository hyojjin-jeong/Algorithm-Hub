import sys
import re #정규 표현식 사용
input = sys.stdin.readline  # 필수로 해놓기

s = input().rstrip()
pattern = re.compile('(100+1+|01)+')
answer = pattern.fullmatch(s)

if answer:
  print("SUBMARINE")
else:
  print("NOISE")