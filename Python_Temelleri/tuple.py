list = [1,2,3]

tuple = 1,'iki',3

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ['ali','veli']
tuple = 'damla','ayşe'
names = ('damla','ayşe') + tuple

print(names)

list[1] = 'davut'
# tuple[1] = 'esra' >>> komutu hatalıdır tuple da elemanlar değiştirilemez.

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))

print(list)
print(tuple)
