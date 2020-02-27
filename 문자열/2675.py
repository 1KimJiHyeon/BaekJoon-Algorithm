T = int(input())

for i in range (T):
  R,S = map(str , input().split())

  for string in S:
    print(string*int(R),end="")
  print()