# 나의 답 - 런타임 에러
A,B=map(int,input().split())

if -10000<=A and B<=10000:
  if A>B:
    print('>')
  elif A<B:
    print('<')
  elif A==b:
    print('==')
  

## 정답 

A,B=map(int,input().split())

if -10000<=A and B<=10000:
  if A>B:
    print('>')
  elif A<B:
    print('<')
  else:
    print('==')