# for i in range(1, 6, 2):
#     print(i)

# word = 'Hallow World!'
#
# for i in word:
#     print(i*3)
# count = 0
# word = 'Hallow World!'
# for i in word:
#     if i == 'l':
#         count += 1
#
# print(f'Count = {count}')

# i = 5
# while i <= 15:
#     print(i)
#     i += 2
#
# is_has_car = True
# i = 5
# while is_has_car:
#     print(i)
#     i += 2
#
# is_has_car = True
# while is_has_car:
#     if input('Введите стоп слово: ') == 'Stop':
#         is_has_car = False

# for i in range(1, 11):
#     if i == 5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)
# found = None
# for i in 'Hallow!':
#     if i == 'r':
#         found = True
#         break
# else:
#     found = False
#
# print(found)


# nums = [1,2,3,4,5, True, 'Hallow']
# nums[0] = 50
# nums[5] = 333
# print(nums)
# print(nums[6])
# ##################################
# nums = [1,2,3,4,5, True, 'Hallow', [1,2,3,4,'Privet']]
# nums[0] = 50
# nums[5] = 333
# print(nums)
# print(nums[6])
# print(nums[7])
# print(nums[-1]) #Последний элемент
# print(nums[7][4])

# numbers = [5, 2, 7]
# # numbers[3] = 100
# numbers.append(100) # [5, 2, 7, 100] добовляет в конце
# numbers.insert(1, True) #[5, True, 2, 7, 100] добовляет в нужном месте
# numbers.extend([5,6,7])# [5, True, 2, 7, 100, 5, 6, 7]  добовляет список к списку
# b = [3, 222, 555]
# numbers.extend(b) # [5, True, 2, 7, 100, 5, 6, 7, 3, 222, 555] добовляет список к списку
#
# numbers.sort() # [True, 2, 3, 5, 5, 6, 7, 7, 100, 222, 555] сортирует
# # numbers.reverse() # [555, 222, 100, 7, 7, 6, 5, 5, 3, 2, True] разворачивает
#
# numbers.pop() # [True, 2, 3, 5, 5, 6, 7, 7, 100, 222] удаляет последний элемент
# numbers.pop(8) # [2, 3, 5, 5, 6, 7, 7, 222] удаляет элемент по индексу
# numbers.remove(True)#  [2, 3, 5, 5, 6, 7, 7, 100, 222] удаляет конкретное значнение
#
# # numbers.clear() # [] очищает список
#
#
#
# print(numbers.count(222)) # считает количество найденых элементов
# print(len(numbers)) #длина списка

# nums = [5, 2, 7, '50', False]
#
# for element in nums:
#     element *= 2
#     print(element)

lens = int(input('Enter lens: '))
i = 0
arr = []
while i < lens:
    string = 'Enter ele,ent #' + str(i + 1) +  ':'
    arr.append(input(string))
    i += 1

print(arr)