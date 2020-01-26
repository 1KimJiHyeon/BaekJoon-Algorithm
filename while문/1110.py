Num = 1
N=input()

if int(N) <10:
    N = "0"+ N

N_i = N

while True:
  
  Nsum = int(N_i[0])+int(N_i[1])

  if Nsum <10:
    Nsum = "0"+str(Nsum)

  else:
    Nsum = str(Nsum)

  New = N_i[1]+Nsum[1]

  if N == New:
    print(Num)
    break
  
  else:
    N_i = New
    Num+=1