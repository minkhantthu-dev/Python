# with open('./k.txt','w') as file:
#     file.write()
#     # Other Work
# with open('./k.txt','a') as file:
#     file.write('\nI am 21 years old')
    
    

list= ['Khant thu hein','\nI am 21 year old']
with open('./k.txt','a') as file:
    file.writelines(list)

