A,B,C=map(int,input().split())

if (2 <= A,B and C <= 10000):
  print((A+B)%C)
  print((A%C + B%C)%C)
  print((A*B)%C)
  print((A%C * B%C)%C)