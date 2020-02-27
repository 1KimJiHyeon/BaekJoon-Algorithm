S = input()
word_list = []
result = []

for word in S:
  word_list.append(word)

for string in "abcdefghijklmnopqrstuvwxyz":
  if string in word_list:
    result.append(word_list.index(string))
  else:
    result.append(-1)

for result_string in result:
  print(result_string,end=" ")