# 나의 답1
bugger = []

for i in range (3):
    bugger.append(int(input()))

coke=int(input())

for coke_price in range(3):
    bugger[coke_price] = bugger[coke_price] +coke-50

soda=int(input())

for soda_price in range(3,len(bugger)):
    bugger[soda_price] = bugger[soda_price] +soda-50

print(min(bugger))

# 나의 답2
bugger = []

for i in range (5):
    bugger.append(int(input()))

bugger_set = []

for coke_price in range(3):
    bugger_set.append(bugger[coke_price] +bugger[3]-50)


for soda_price in range(3):
    bugger_set.append(bugger[soda_price] +bugger[4]-50)

print(min(bugger_set))