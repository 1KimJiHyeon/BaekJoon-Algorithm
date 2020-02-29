# 나의 답

N = int(input())

if N%3 != 0 and N%5 !=0:
  print(-1)

elif N%5 == 0 :
  print(N//5)

elif N%5 != 0 or 3 :
  print((N//5) + ((N//5)//3))

else:
  print(N//3)

# 답
sugar = int(input()) 
count = 0 
while True:
  if (sugar % 5) == 0: 
     count = count + (sugar//5) 
     print(count) 
     break
  sugar -= 3 
  count += 1 
  if sugar < 0:
     print("-1") 
     break
