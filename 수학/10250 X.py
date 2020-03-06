# 나의 답

T = int(input())

for i in range(T):
  
  H,W,N = map(int,input().split())
  x=0
  y=1
  if N%H == 0:
    x=H
  else:
    x=N%H

  y+=N//H
  if y >W:
    x+=1
    
    if x>H:
      x=1
      y+=1


  if y<10:
    y="0"+str(y)
  print(str(x)+str(y))

  # 답

  T = int(input())
for i in range(T) :
    H, W, N = map(int, input().split())
    print(str(N%H)+str(N//H+1).zfill(2) if N%H!=0 else str(H)+str(N//H).zfill(2))