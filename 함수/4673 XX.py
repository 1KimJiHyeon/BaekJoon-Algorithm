# 고민중..

def self_num():
  
  nums = 1
  while nums <=10000:

    num_total = 0

    if len(str(nums))>=2:
      for num in str(nums):
        num_total +=num

    num_total+=nums
    print(num_total)
    


print(self_num())
