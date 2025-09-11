# key - value >>> bir key bilgisine ulaşmak için value bilgisini kullanıyoruz .

# 41 =>  kocaeli    34 => İstanbul  gibi

# sehirler = ['kocaeli','istanbul']
# plakalar = [ 41 , 34 ]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli']) => 41 
# print(plakalar['istanbul']) => 41 

# plakalar = {'kocaeli' : 41 , 'istanbul' : 34 }

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['Ankara'] = '06' 
# print(plakalar['Ankara'])

# print(plakalar)

users = {
    'Sadik Turan' : {
        'age' : 36,
        'roles': ['user'], 
        'email' : 'sadik@gmail.com',
        'adress' : 'kocaeli', 
        'phone' : '12345678910'
    },
    'Cinar Turan' : {
        'age' : 20,
        'roles': ['admin','user'], 
        'email': 'cinar@gmail.com',
        'adress' : 'kocaeli', 
        'phone' : '123456'
    },
}

print(users['Sadik Turan']['age'])
print(users['Cinar Turan']['adress'])
print(users['Cinar Turan']['email'])
print(users['Cinar Turan']['roles'][0])
print(users['Sadik Turan']['roles'])

