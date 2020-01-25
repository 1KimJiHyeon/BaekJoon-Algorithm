# T = int(input())

# for i in range (T):
#   A,B = map(int,sys.stdin.readline().split())
#   print(A+B)


## 정답 - import sys
import sys

for i in range (int(input())):
  A,B = map(int,sys.stdin.readline().split())
  print(A+B)
