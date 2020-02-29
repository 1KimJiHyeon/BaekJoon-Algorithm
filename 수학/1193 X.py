# 답 - 고민중..

a=int(input())
i=1
while i<a:
    a-=i
    i+=1
if i%2==0:
    print("%d/%d" %(a,i-(a-1)))
else:
    print("%d/%d" %(i-(a-1),a))