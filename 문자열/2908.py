first_num , second_num = map(str,input().split())

first=""
second =""

for i in range (len(first_num)-1,-1,-1):
  first+=first_num[i]

for j in range (len(second_num)-1,-1,-1):
  second+=second_num[j]

check=[first,second]
print(max(check))