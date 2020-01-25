# 나의 답
N,X = map ( int, input().split())
list =[]

for i in range (N):
  num = int(input())
  if num<X:
    list.append(num)
  else:
    pass
for j in list:
  print(j,end=" ")

# 정답 - list 한 번에 받는 방법을 몰랐음

N,X = map ( int, input().split())
numlist = list(map(int, input().split()))

list=[]
for i in range (N):
  if numlist[i]<X:
    list.append(numlist[i])
  else:
    pass

for j in list:
  print(j,end=" ")
