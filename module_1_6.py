my_dict = {'dog': 'Абрикос', 'cat': 'Байкер', 'parrot': 'Рики'}
print(my_dict)
print(my_dict ['cat'])
print(my_dict.get('snake')) # вывод отсутствующего эл-та (без ошибки)

my_dict.update({'humster': 'Элвин',
                'mouse': 'Джерри'})
print(my_dict)
del my_dict['parrot']
print(my_dict)

my_set = {'Masha', 3, 'Petya', 'Masha', 4, 4, 0.5, 'Masha'}
print(my_set)
my_set.add('Ready')
my_set.add((1, 4, 7))
print(my_set)
my_set.discard('Petya')
print(my_set)
# print(my_set.discard('Petya'))
my_set.pop()
print(my_set)