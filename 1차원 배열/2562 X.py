# 나의 답
numlist = list(map(int,input().split()))

print(max(numlist))
print(numlist.index(max(numlist))+1)


# 정답 - 한 줄에 하나의 자연수가 주어진다는 문제의 조건을 지나침
numlist = []
for i in range (9):
  numlist.append(int(input()))

print(max(numlist))
print(numlist.index(max(numlist))+1)