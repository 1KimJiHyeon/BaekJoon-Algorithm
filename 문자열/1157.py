words = input().upper()
words_list = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for word in alphabet:
  if word in words:
    words_list.append(words.count(word))
  else:
    words_list.append(words.count(word))

sum = 0

for i in range (len(words_list)):
  if max(words_list) == words_list[i]:
    sum+=1

if sum >=2:
  print("?")
else:
  print(alphabet[words_list.index(max(words_list))])