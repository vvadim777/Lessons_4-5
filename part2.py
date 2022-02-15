from collections import Counter
person = [
    {
        'name': 'Vadim',
        'age': 30,
        'gender': 'male'
    }, {
        'name': 'Olga',
        'age': 54,
        'gender': 'female'
    }, {
        'name': 'Sasha',
        'age': 21,
        'gender': 'male'
    }, {
        'name': 'Dima',
        'age': 17,
        'gender': 'male'
    }, {
        'name': 'Vera',
        'age': 25,
        'gender': 'female' 
    }, {
        'name': 'Fedor',
        'age': 34,
        'gender': 'male' 
    }, {
        'name': 'Igor',
        'age': 33,
        'gender': 'male'
    }, {
        'name': 'Franc',
        'age': 62,
        'gender': 'male'
        }, {
        'name': 'lena',
        'age': 33,
        'gender': 'female'   
        }, {
        'name': 'Oleg',
        'age': 23,
        'gender': 'male'
        }, {
        'name': 'Sveta',
        'age': 18,
        'gender': 'female'  
        },{
        'name': 'Oleg',
        'age': 22,
        'gender': 'male'  
        }, {
        'name': 'Olga',
        'age': 33,
        'gender': 'female'
        }, {
        'name': 'Sasha',
        'age': 53,
        'gender': 'male'
        }
]


print(len(person)) # количество всех людей

print([st['name'] for st in person]) # список имен

a = ([st['gender'] for st in person]) # количество мужчин и женщин
count=Counter(a)
print(count)

name = ([st['name'] for st in person])
count_name=Counter(name)
print(count_name.most_common(3)) #три самых популярных имени

age = [ag["age"] for ag in person if ag["age"]>=18]
print(len(age)) #количество несовершеннолетних

vozrast = [ag["age"] for ag in person] # список всех неповторяющихся возрастов
vozrast_1=list(set(vozrast))
vozrast_1.sort()
print(vozrast_1)
