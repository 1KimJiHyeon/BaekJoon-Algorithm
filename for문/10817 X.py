#나의 답
A,B,C = map(int,input().split())

if A>B:
  if B>C:
    print(B)
  elif B<C:
    if A>C:
      print(C)
    else:
      print(A)
else:
  if A>C:
    print(A)
  elif A<C:
    if C<B:
      print(C)
    else:
      print(B)

## 정답 - 숫자가 전부 같을 때를 고려 안 함
A,B,C = map(int,input().split())

if A>=B:
  if B>=C:
    print(B)
  elif B<C:
    if A>=C:
      print(C)
    else:
      print(A)
else:
  if A>=C:
    print(A)
  elif A<C:
    if C<=B:
      print(C)
    else:
      print(B)