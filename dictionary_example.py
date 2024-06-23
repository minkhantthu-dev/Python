person = {}
# loop ပတ်ချင်ရင် item ဆွဲထုတ်
# name = input('name :')
# age = input('age :')

# person[name] = age

while True :
    name = input('name :')
    age = input('age :')

    person[name] = age
    
    another = input('anoter y/n:')
    if another == 'y' :
        continue;
    else:
        break;

# for (key,value) in person.items() :
#     print(f'{key} is {value} years old.')

ages = list(person.values())

for age in set(ages):
    count = ages.count(age)
    print(f'{age} years old - {count} ');
