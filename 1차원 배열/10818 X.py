# 나의 답 - 왜 틀렸는지 솔직히 모르겠음 (찾아보니 C에서는 split이 없기때문에 N 제공)
N = int(input())
numlist=[]



for i in range(N):
  num=int(input())
  numlist.append(num)

for num in numlist:
  print(num,end=" ")
print("")

print(min(numlist),max(numlist))

#정답
n = int(input())
ns = list(map(int, input().split()))
print("{} {}".format(min(ns), max(ns)))
