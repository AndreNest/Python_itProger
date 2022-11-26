# country = {'code':'RU','name' : 'Russian', 'population' : 144000000}
# country = dict(code='RU', name='Russian', population='144000000')
# print(country['name'])
# print(country)
#
# for key, value in country.items():
#     print(key, '-', value)

# country = {'code':'RU','name' : 'Russian', 'population' : 144000000}
# print(country['code'])
# print((country.get('name')))
# # country.clear()
# # print(country)
# # country.pop('name')
# # country.popitem() # удаляет последний элемент!
# print(country)
# print(country.keys())
# print(country.values())
# print(country.items())
#
# country['code'] = 'RUSSIK'
# print(country)

person = {'user_1':
              {'first_name': 'John',
               'last_name' : 'Morley',
               'age' : 45,
               'adress' : ['г. Москва', 'ул. Плеханова' , 29],
               'grades' : {'match' : 5, 'phisic' : 3} } ,
          'user_2':{} }

print(person['user_1']['adress'][1])