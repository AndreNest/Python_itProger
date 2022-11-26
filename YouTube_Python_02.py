data = (4, 6, 7, 3, 6, True, 5.6, 'Hallo')
# data[0] = 0 КОРТЕЖИ НЕИЗМЕНЯЕМЫ!
print(data[1])
print(data[1:5])

print(data.count(6))
print(len(data))
print(data)

data_1 = 4, 6, 7, 3, 6, True, 5.6, 'Hallo'
print(data_1)
data_2 = (5) # не кортеж
data_3 = (5,) #кортеж

data_6 = 4, 6, 7, 3, 6, True, 5.6, 'Hallo'

for i in data_6:
    print(i)

nums = [5, 7, 8]
print(nums)
new_date = tuple(nums)
word = tuple('Hallow word!')
print(new_date)
print(word)
