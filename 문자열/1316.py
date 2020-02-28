N = int(input())
N_list = []

for i in range (N):
  N_list.append(input())

N_sum = len(N_list)

for j in range(len(N_list)):
  for k in range (len(N_list[j])-1):
    if N_list[j][k] != N_list[j][k+1]:
      if N_list[j][k] in N_list[j][k+1:]:
        N_sum-=1
        break

print(N_sum)