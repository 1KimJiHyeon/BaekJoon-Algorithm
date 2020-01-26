#나의 답
for i in range (1,int(input())+1):
  for j in range (0,1):
    A,B = map(int,input().split())
    print("Case #"+str(i)+":",str(A+B))

# 정답 - for문 밑으로만 반복 된다 input 다시 받지 않음
T = int(input())
for i in range (1,T+1):
    A,B = map(int,input().split())
    print("Case #"+str(i)+":",str(A+B))