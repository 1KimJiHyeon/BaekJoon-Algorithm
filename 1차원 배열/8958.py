testcount = int(input())

for i in range (testcount):
  test = input()
  sum=0
  count=0
  for word in test:
    if word == "O":
      count+=1
    if word=="X":
      count = 0
    sum+=count
  print(sum)


