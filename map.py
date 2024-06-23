# list တွေကို overwrite

nums = [1,2,3,4,5,6,7,8,9,10]

# map(function,list)   
# nums = (list(map(mapfunction,nums)))
# print(nums)

def mapfunction(num) :
    return num*2
print(list(map(mapfunction,nums)))


# nums = [num*2 for num in nums]
# print(nums)                       #comprehension




nums = (list(map(lambda num:num*2,nums)))  #Lambda function
print(nums)