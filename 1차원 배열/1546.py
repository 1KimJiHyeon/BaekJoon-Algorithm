N = int(input())

score = list(map(int,input().split()))
fake = []

for i in score:
  fake.append(i/max(score)*100)

# sum 함수
faketotal =0
for k in fake:
  faketotal+=k

print(faketotal/N)