word_dict = {}

for word in "ABC":
  word_dict[word] = 3
for word in "DEF":
  word_dict[word] = 4
for word in "GHI":
  word_dict[word] = 5
for word in "JKL":
  word_dict[word] = 6
for word in "MNO":
  word_dict[word] = 7
for word in "PQRS":
  word_dict[word] = 8
for word in "TUV":
  word_dict[word] = 9
for word in "WXYZ":
  word_dict[word] = 10

nums = input()
nums_count = 0

for i in nums:
  nums_count+=word_dict[i]
  
print(nums_count)