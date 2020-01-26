# 나의 답
H,M = map(int,input().split())

if 0<=H<=23 and 0<= M <= 59:
  Alarm = H*60 + M - 45
  H = Alarm//60
  M = Alarm%60
  print(H,M)

## 정답 - 0을 고려 안 함

H,M = map(int,input().split())

if 0<=H<=23 and 0<= M <= 59:
  if H==0:
    H=24
  else:
    pass
  Alarm = H*60 + M - 45
  H = Alarm//60
  M = Alarm%60
  print(H,M)
