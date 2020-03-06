# 나의 답 - 시간초과

A,B,V = map(int,input().split())

sum=0
count=0

while True:
  sum+=A
  count+=1
  if sum >=V:
    
    break
  else:
    
    sum-=B
print(count)

# 답
A,B,V = map(int,input().split())

Day = (V-B) / (A-B)

if Day == int(Day):
  print(int(Day))
else:
  print(int(Day)+1)