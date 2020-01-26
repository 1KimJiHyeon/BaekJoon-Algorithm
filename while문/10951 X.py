#나의 답
while True:
  A,B = map (int, input().split())
  print(A+B)

## 정답 -> EOF
while True:
  try:
    A,B = map (int, input().split())
    print(A+B)
  except:
    break