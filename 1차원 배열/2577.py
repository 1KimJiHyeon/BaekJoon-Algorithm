# 나의 답 - count 함수를 까먹고 있었다.

numlist = []
for i in range (3):
  numlist.append(int(input()))

A = numlist[0]
B = numlist[1]
C = numlist[2]

total = str(A*B*C)

totalnumlist = []
zero = 0
one = 0
two = 0
three = 0
four= 0
five = 0
six = 0
seven = 0
eight= 0
nine = 0


for num in total:
  if num == "0":
    zero+=1
  if num == "1":
    one+=1
  if num == "2":
    two+=1
  if num == "3":
    three+=1
  if num == "4":
    four+=1
  if num == "5":
    five+=1
  if num == "6":
    six+=1
  if num == "7":
    seven+=1
  if num == "8":
    eight+=1
  if num == "9":
    nine+=1
print(zero)
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)

# 모범 답안
a = int(input())
b = int(input())
c = int(input())

ans = a*b*c
ansstr = str(ans)

for i in range(0,10):
   print(ansstr.count(str(i)))