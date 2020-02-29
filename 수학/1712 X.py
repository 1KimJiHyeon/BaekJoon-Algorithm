# 나의 답 - 시간 초과

A,B,C = map(int,input().split())
x = 1
while True:
  if A+B*x < C*x:
    print(x)
    break
  
  else:
    if x>2100000000:
      print(-1)
      break
    else:
      x+=1

# 정답

A,B,C = map(int,input().split())

if B>=C:
  print(-1)
else:
  print(int(A/(C-B)+1))