# 나의 답 - 런타임 에러 , replace를 쓸 것

words = input()

words_count = len(words)

for i in range( len(words)):
  if words[i] == "c":
    if words[i+1] == "=" or "-":
      words_count-=1
  if words[i] == "d":
    if words[i+1] == "-":
      words_count-=1
    if words[i+1] == "z":
      if words[i+2] == "=":
        words_count-=2
  if words[i] == "l":
    if words[i+1] == "j":
      words_count-=1
  if words[i] == "n":
    if words[i+1] == "j":
      words_count-=1
  if words[i] == "s":
    if words[i+1] == "=":
      words_count-=1
  if words[i] == "z":
    if words[i-1] != "d":
      if words[i+1] == "=":
        words_count-=1
  else:
    words_count+=0
  
print(words_count)

# 답

words = input()
words = words.replace("dz=","1")
words = words.replace("c=","1")
words = words.replace("c-","1")
words = words.replace("d-","1")
words = words.replace("lj","1")
words = words.replace("nj","1")
words = words.replace("s=","1")
words = words.replace("z=","1")
print(len(words))