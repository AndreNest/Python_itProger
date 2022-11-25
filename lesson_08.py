# word = 'hallow,world,!,mother,f*ck'
# print(word[5]) # w
# print(len(word)) #13
# print(word.count('l')) # 3
# print(word.upper()) # HALLOW WORLD!
# print(word.isupper()) #False
# word = 'HALLOW WORLD!'
# print(word.isupper()) #True
# word = 'hallow,world,!,mother,f*ck'
# print(word.islower())
# print(word.capitalize())
# print(word.find('l'))
# print(word.split(','))
# hoby = word.split(',')
# print(hoby[4])
#
# for i in range(len(hoby)):
#     hoby[i] = hoby[i].capitalize()
# print(hoby)
#
# result = ', '.join(hoby)
# print(result)
# СРЕЗЫ#########################################
word = 'Football'

print(word[0:4]) #Foot
print(word[4:]) #ball
print(word[1:-1:2]) #ota

list = [6, 4, "Stroka", True, 6.5]
print(list[2]) # Stroka
print(list[2:]) #['Stroka', True, 6.5]
print(list[2:-1]) #['Stroka', True]
print(list[2:-2]) #['Stroka']
print(list[::2]) #[6, 'Stroka', 6.5]
print(list[::-1]) #[6.5, True, 'Stroka', 4, 6] разворот списка
