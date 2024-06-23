def greet(fun):
    
    def rapper():
        print('hello')
        fun()    #before
        
        print('good bye')  #after
        
    return rapper
    
    
@greet
def sayName():
    print('Khant thu hein')
    
sayName()


# def greet(fun):
    
#     def rapper(name):
#         print('hello')
#         fun(name)    #before
        
#         print('good bye')  #after
        
#     return rapper
    
    
# @greet
# def sayName(name):
#     print(name)
    
# sayName('kk')