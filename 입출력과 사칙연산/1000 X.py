#나의 답
A = int(input("정수를 입력해주세요"))
B = int(input("정수를 입력해주세요"))

if 0<A and B<10 :
  print(A+B)

#정답
## 첫째 줄에 A와 B가 주어져야한다.
a, b = map(int, input().split())
print(a+b)