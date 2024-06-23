# prices = {2000,1000,3000}

# double_prices = []
# for price in prices:
#     double_prices.append(price*2)     #normal code    
# print(double_prices);



prices = {2000,1000,3000}
double_prices = [price*2 for price in prices]   # best code
print(double_prices);

# nums = [1,2,3,4,5,6]
# even_double_nums = []
# for num in nums:
#     if(num%2) == 0 :
#         even_double_nums.append(num*2)
        
# print(even_double_nums)

nums = [1,2,3,4,5,6]
even_double_nums = [num*2 for num in nums if (num%2)==0]
print(even_double_nums)