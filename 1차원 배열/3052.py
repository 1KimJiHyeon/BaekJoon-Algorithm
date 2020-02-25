# 나의 답 - set 함수를 까먹음
numlist = []
for i in range (10):
  numlist.append(int(input())%42)


checklist=0

for k in range(0,42):
  
  if numlist.count(k) >= 2:
    checklist+=1

print(len(numlist)-checklist)

# 답
num_list = list() 
for _ in range(10): 
  num = int(input()) 
  num_list.append(num % 42) 
num_list = set(num_list) 
print(len(num_list))
