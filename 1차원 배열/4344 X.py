# 나의 답 = 반올림하여 소수점 셋째 자리까지 출력한다 조건을 놓침
C =int(input())

for i in range (C):
  score = list(map(int,input().split()))
  scoresum =0
  count = 0
  for k in range (1,len(score)):
    scoresum+=score[k]
  for j in range (1,len(score)):
    if score[j] > (float(scoresum)/float(score[0])):
      count+=1
  print(str(count/score[0]*100)+"%")


# # 답
# C =int(input())

# for i in range (C):
#   score = list(map(int,input().split()))
#   scoresum =0
#   count = 0
#   for k in range (1,len(score)):
#     scoresum+=score[k]
#   for j in range (1,len(score)):
#     if score[j] > (scoresum/score[0]):
#       count+=1
#   print("%0.3f%%" %round(count/score[0]*100 ,3))
