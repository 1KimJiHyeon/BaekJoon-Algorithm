# 답 - 고민중..
n = int(input())
arr=[1]
i=0

while arr[i] < 1000000001:
  i+=1
  arr.append(arr[i-1]+6*i)

arr.append(n)
arr.sort()
print(arr.index(n)+1)