nums = [1,2,3,4,5,6,7,8,9,10]

# filter(functon,list)

# def even(num):
#     return(num%2) == 0 

# print(list(filter(even,nums)))

# nums = [num for num in nums if (num%2) == 0] 
# print(nums)

evenNums = []
for num in nums:
    if (num%2) == 0:
        evenNums.append(num);
        
print(evenNums)