#While - задача №3
# i = input('p = ')
# i = float(i) - float(i)//1
# j = 0
# while(i>0):
#     j+=1
#     print(i)
#     i*=10
#     i = (i) - (i)//1
# print(j)
#==========================================

# i = int(input('сколько дней в месяце = '))
# j = 0
# while(i!=0):
#     if i%2 != 0:
#         j+=1
#     i = int(input('сколько дней в месяце = '))
# print(j)


# while(True):
#     i = int(input('номер билета = '))
#     if(i==0):
#         break
#     j = i//1000
#     i = i%1000
#     if(i%10+i%100//10+i//100 == j%10+j%100//10+j//100):
#         print('win')
#     else:
#         print('lose')

# p = 0
# o = 0
# while(True):
#     i = int(input('число = '))
#     if(i==0):
#         break
#     if(i > 0):
#         p+=1
#     else:
#         o+=1
#
# print(p)
# print(o)

# j = 0
# i = 0
# m = 0
# while(j<=8):
#     j+=1
#     i+= int(input('сколько задач = '))
#     z = int(input('zvonok: '))
#     if(z == 1):
#         m = 1
# print(f'sdelal  {i} zadach')
# if( m == 1):
#     print('magazin idi')


# x = int(input('x = '))
# p = int(input('p = '))/100+1
# z = int(input('z = '))
# l = 0
# while(x<z):
#     x = x * p
#     l+=1
# print(l)

# #while десятая задача №10========================================
# bottom = 0
# top = 100
# third = 0
# guessed = int(input('zagadai chislo: '))
# number = 50
# while True:
#     print(bottom, top)
#     otvet = int(input(f'Твое число =(1), >(2), <(3) {number}?  '))
#     if(otvet == 1) and number == guessed:
#         print('вы угадали число')
#         break
#     elif(otvet == 2):
#         bottom = number + 1
#         number = (bottom + top)//2
#     elif(otvet == 3):
#         top = number - 1
#         number = (bottom + top)//2
# #===============================================================\

# for i in 114, 12, 14, 10605, 4907, 450:
#     if i%2 == 0 and i%3 != 0:
#         print(f'{i}  podhodit')
#     else:
#         print(f'{i}  nepodhodit')

import random
# j = 0
# for i in range(10):
#     n = random.randint(-100,100)
#     if n%2 == 0 and n>0:
#         j+=1
# print(j)


# z = 0
# for i in range(12):
#     z += random.randint(100000,170000)
# print(z/12)

# n = 0
# for i in range(6):
#     if random.randint(0,15) > 10:
#         print(f'в секторе {29+i} нарушение, людей больше 10!')
#         n+=1
# print(f"количество нарушений = {n}")

#Факториал задача №5===========================================================
# f = 1
# for i in range(1,int(input('факториал какого числа надо найти?'))+1):
#     f = i*f
# print(f)
#===============================================================================

# t = 0
# h = 0
# o = 0
# for i in range(1,random.randint(10,30)+1):
#     if random.randint(3,5) == 3:
#         t += 1
#     if random.randint(3,5) == 4:
#         h += 1
#     if random.randint(3,5) == 5:
#         o += 1
# s = {'троечники': t, 'хорошисты': h, 'oтличники' : o}
# print(s)
# print(max(s.items()))

# t = 0
# j = 0
# a = int(input('perv = '))
# b = int(input('vtoroe = '))
# for i in range(a, b):
#     if i % 3 == 0:
#         print(i)
#         j+=i
#         t+=1
# print(j/t)


# for i in range(10,100):
#     if i//10*i%10*3 == i:
#         print(i)

# j = 0
# for i in range(10):
#     z = random.randint(100, 150)
#     print(z)
#     if z>j:
#         j = z
#     else:
#         o = 1
#         break
# if o != 1:
#     print('все норм')
# elif o == 1:
#     print('обман')


# N = int(input('N = '))
# for i in range(1, N+1):
#     if int(input('vvedite sled nomer: ')) != i:
#         print(f'потеряна карточка номер {i}')


# for i in range(100, -4, -4):
#     print(i)
#     if i == 0:
#         print('end')


# for i in range(0, int(input('skolko doljnikov?  ')), 5):
#     print(f'Человек номер {i} должен еще {random.randint(1,300)} тыс. руб.')


# for i in range(60, -30, -30):
#     if i <= 0:
#         print('end')
#     o = int(input(f'осталось {i}. Xотите обезвредить? нет(0) да(1) '))
#     if o == 1:
#         print(f'обезврежена за {60-i} секунд')


# a = int(input('perv = '))
# b = int(input('vtoroe = '))
# c = 3#random.randint(2,5)
# s = 0
# j = 0
# for i in range(a, b+1):
#     if i%c == 0:
#         s += i
#         j+=1
# print(s/j)



# a = int(input('perv = '))
# b = int(input('vtoroe = '))
# c = -3#random.randint(2,5)
# s = 0
# j = 0
# for i in range(b, a+c, c):
#     print(i)
#     print(i**3 + i**2*2 - 4*i + 1)

#складывание листа задача 6==========================================
# l1 = int(input('l1 = '))
# l2 = int(input('l2 = '))
# r = 0
# q = 0
# w = 0
# if l1 == 12:
#     q = -1
# if l2 == 12:
#     w = -1
# for i in range(int(l1/12)+q+int(l2/12)+w):
#     r+=1
# print(f'лист надо сложить {r} раз')


# g = 2300
# e = 18000
# p = 0
# for i in range(10):
#     p += e - g
#     e *= 1.03
# print(e)
# print(p)

# n = int(input('n = '))
# s = 0
# for i in range(n):
#     s += (-1)**(i)/2**i
#     print(s)


#сумма ряда задача №9====================================================
# x = 0
# s1 = 1
# s2 = 1
# sh = 1
# sh2 = 2
#
# for i in range(1,7,sh):
#     #print(sh)
#     s1 = (x - sh) * s1
#     sh = 2*sh+1
# print(s1)
#
# for i in range(1,13,sh2):
#     #print(sh2)
#     s2 = (x - sh2) * s2
#     sh2 = 2*sh2
# print(s2)
# print(s1/s2)
# ==================================================================

# Цикл for задача 10 - рассадка мальчиков и девочек
# b = int(input('введите число boys: ))
# g = int(input('введите число girls: ))
# s = ''
# d = float(b/g)
# d1 = float(g/b)
# print(d)
# if d > 2 or d1 > 2:
#     print('невозможно')
# if d>1:
#     for i in range(b-g):
#         s += 'BGB'
#         g -= 1
#     for i in range(g):
#         s += 'BG'
# if d1>1:
#     for i in range(g-b):
#         s += 'GBG'
#         b -= 1
#     for i in range(b):
#         s += 'GB'
# print(s)


# ================================================
#9.6  Задача 1. Календарь

# j = 0
# w = {'понедельник' : 1, 'вторник': 2,'среда' : 3,'четверг' : 4,'пятница' : 5,'суббота' : 6,'воскресенье' : 7}
# d = input('введите день недели:  ')
# for i in w.keys():
#     if d == i:
#         print(w[i])
#??????
# j = 0
# w = ('понедельник', 'вторник','среда','четверг','пятница','суббота','воскресенье')
# d = input('введите день недели:  ')
# for i in w:
#     j+=1
#     if d == i:
#         print(j)


#Задача 2. Я стал новым пиратом!
# j = 0
# w = ('понедельник', 'вторник','среда','четверг','пятница','суббота','воскресенье', 'карамба', 'карамба')
# for i in w:
#     if i == 'карамба':
#         j+=1
# print(j)


#Задача 3. Кривой мессенджер
# s = 'Нккоаркао *ТГУТ*тауауо'
# for j,i in enumerate(s):
#     if i == '*':
#         print(j)


#Задача 4. Театр

# r = 5
# s = 7
# m = 3
# for i in range(r):
#     print('='*s + '*'*m + '='*s)


#Задача 5. Марсоход 2

# x = 15
# y = 20
# x1 = 8
# y1 = 10
#
# while True:
#     k = input(f'Марсоход находится на позиции {x1}, {y1}, введите команду:')
#     if k == 'a' and x1 != 0:
#         x1 -= 1
#     if k == 'w' and y1 != y:
#         y1 += 1
#     if k == 's' and y1 != 0:
#         y1 -= 1
#     if k == 'd' and x1 != x:
#         x1 += 1


# Задача 6. Спецшифр

# c = 'assssssldldlrfrsssssssssssssfrfrss'
# j = ''
# max = 0
# m = 1
# for i in c:
#     if i == 's' and j == 's':
#         m = m+1
#     elif m > max and i != 's':
#         max = m
#         m = 1
#     j = i
# print(max)


#Задача 7. Великий и могучий

# c = ' aedd  sss ssslssss  sssedededdes sfrfrss                 '
# j = 0
# max = 0
# for i in c:
#     if i != ' ':
#         j += 1
#     elif i == ' ' and j > max:
#         max = j
#         j = 0
# print(max)


#Задача 8. Колонтитул

# d = 11
# v = 4
# p = int((d-v)/2)
# if v<d:
#     print('-'*p+'!'*v+'-'*p)


# Задача 9. Коровы

# s = 'abababaabb'
# p = 2
# m = 0
# for i in s:
#     if i == 'a':
#         m += p
#     p+=2
# print(m)


# Задача 10. Метод бутерброда

# s = 'shacnidw'
# d = len(s)
# p = ''
# for i in range(0,d,2):
#     p += s[i]
# for i in reversed(range(1,d,2)):
#     p += s[i]
# print(p)


#10.6 Практическая работа==============================================

#Задача 1. Тестовое задание
# b = 0
# d = 10
# for i in range(0,6):
#     for j in range(b,d+1, 2):
#         print(j,end=' ')
#     print('\n')
#     b+=1
#     d+=1


# Задача 2. Лестница

# N = 5
# for i in range(1,7):
#     for j in range(1,i):
#         print(j,end=' ')
#     print('\n')


# Задача 3. Рамка

# s = 4
# v = 4
# print('|',end='')
# for i in range(s):
#     print('-',end='')
# print('|')
# for i in range(v-2):
#     print('|' + ' '*s + '|')
# print('|',end='')
# for i in range(s):
#     print('-',end='')
# print('|')


# Задача 4. Крест

# for i in range(8+1):
#     for j in range(8+1):
#         if i == j or i == 8-j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print('\n')


#Задача 5. Простые числа
# n = (13,2,4,5,7,8,14,72,37)
# s = 0
# p = (2,3,5,7,9,11,13,17,19,23,29,31,37,41)
# for i in n:
#     for j in p:
#         if i == j:
#             s+=1
# print(s)


# Задача 6. Сумма факториалов

# n = 3
# s = 0
# f = 1
# for i in range(1,n+2):
#     f = 1
#     for j in range(1,i+1):
#         f *= j
#     s+=f
# print(s)


# Задача 7. Наибольшая сумма цифр

# c = (123,4324,245524,65365,332156616,444,31)
# s = 0
# m = 0
# for i in c:
#     s = 0
#     i = str(i)
#     for j in range(len(i)):
#         s += int(i[j])
#     print('\n')
#     if s > m:
#         m = s
# print(m)


#Задача 8. Пирамидка

# v = 8 # вводимая высота, остальные константы
# s = 1
# p = 2*v
# for i in range(1, 2*v, 2):
#     print(' '*int(p/2),end='')
#     print('#'*i)
#     print(' '*int(p/2),end='\n')
#     p -= 2


#Задача 9. Пирамидка 2

# v = 5
# s = 2*v + 1
# x = 1
# d = 1
# c = 1
# br = 0
# for i in range(1,v):
#     for j in range(1, 2*v, 1):
#         print('    ',end='')
#         if j == v and x in (1,9,25):
#             print(x,end='')
#             print(8,end='')
#             x += 2
#         if j == v-d and i > 1:
#             print(x,end='')
#             print(7, end='')
#             x += 2
#             d += 1
#         if j == v-d/(i/2) and
#         if j == v+c and i > 1:
#             print(x,end='')
#             print(9, end='')
#             x += 2
#             c += 1
#             br += 1
#             if br >= i/2:
#                 break
#     print('\n')





# v = 4
# s = 2*v
# str = 1
# for i in range(v):
#     print(str,end='')
#     str+=1
#     for j in range(s+1):
#         if j == v and i%2 != 1:
#             print('xс',end='')
#         if i == v and j == 0: #угол
#             print('xг1', end='')
#         if i == v and j == s: #угол
#             print('xг2', end='')
#         if j == v/(i+1) and i !=0:
#             print('x', end='')
#         # if j == s/(i+1):
#         #     print('x', end='')
#         print('  ', end='')
#     print('\n')

#Задача 10. Яма

# g = 7
# t = 0
# for i in range(1,g+1):
#     #print(g, end='')
#     t = i
#     c = g
#     countm = 0
#     countp = 0
#     for j in range(1,2*g):
#         if countm < g and countp < g:
#             countm += 1
#             countp += 1
#             if j > i:
#                 print('.',end='')
#             elif j < i+1:
#                 print(c, end='')
#             if c > 1:
#                 c -= 1
#         if countp >= g:
#             if j-g > g-i-1:
#                 print(c, end='')
#             else:
#                 print('.', end='')
#             c += 1
#     print('\n')



#11.6 Практическая работа

#Задача 1. Конвертация

# p = float(input('введите сумму в евро:'))
# s = p*1.25*60.87
# print(s)


import math

#Задача 2. Грубая математика

# N = [23,2.7,-5.4,-7.1,-9,43.2]
# M = []
# for j, i in enumerate(N):
#     if N[j] >= 0:
#         N[j] = math.log(math.ceil(N[j]))
#     if N[j] < 0:
#         N[j] = math.exp(math.floor(N[j]))
# print(N)


# Задача 3. Убийца Steam

# s = 274
# c = 18
# t = math.ceil(s/c)
# for i in range(t):
#     print(f'прошло {i}, скачано {i*c} мегабайт из {s}: {round((i*c)/s*100)}%')
# print(f'прошло {t} секунд')


# Задача 4. Первая цифра

# x = 25.7438
# print(int(x%1*10//1))


# Задача 5. Вот это объёмы!

# rs = 3389.5
# vz = 10.8321*10**11
# vs = 4/3*math.pi*rs**3
# print(round(vz/vs,3))


# Задача 6. Метеостанция

# n = -35#int('n = ')
# v = 18#int('v = ')
# s = 4#int('s = ')
#
# for i in range(n, v+1, s):
#     print(f'{i}C = {round(32+1.8*i)}F')
# print(f'{v}C = {32+1.8*v}F')


# Задача 7. Ход конём

# x1 = 0.043
# y1 = 0.13
# x2 = 0.24
# y2 = 0.0245
# while True:
#     if abs(round(x1,1) - round(x2,1)) == 0.2 and abs(round(y1,1) - round(y2,1)) == 0.1:
#         print(f'конь в клетке ({round(x1*10)},{round(y1*10)}). Точка в клетке ({round(x2*10)},{round(y2*10)}) \n Ход возможен')
#         break
#     elif abs(round(x1,1) - round(x2,1)) == 0.1 and abs(round(y1,1) - round(y2,1)) == 0.2:
#         print(f'конь в клетке ({round(x1 * 10)},{round(y1 * 10)}). Точка в клетке ({round(x2 * 10)},{round(y2 * 10)}) \n Ход возможен')
#         break
#     else:
#         print('no')
#         break


# Задача 8. Часы

# a = 75
#
# g = round(a/(360/12)%1*(360/12))
#
# print(g)

import math
# Задача 9. Уравнение
#
# a = 3
# b = 8
# c = 5
# if b**2 - 4*a*c >= 0:
#     D = b**2 - 4*a*c
#     x1 = (-b+D**0.5)/(2*a)
#     x2 = (-b-D**0.5)/(2*a)
#     if x1 == x2:
#         print(x1)
#     else:
#         print(x1,x2)
# else:
#     print('нет корней')


# Задача 10. За что?

# from math import sqrt
# m = 2; n = 8
#
# try:
#     sqrt(m - n)
#     print(m)
# except ValueError:
#     print(n)



# 12.6 Практическая работа

# Задача 1. Сумма чисел

# def summa_n(n):
#     p = 0
#     for i in range(n+1):
#         p +=i
#     return p
#
# N = 3
# print(summa_n(N))


# Задача 2. Функция в функции

# def positive():
#     print('положительное')
#
# def negative():
#     print('отрицательное')
#
# def test(c):
#     if c > 0:
#         positive()
#     if c < 0:
#         negative()
#
# test(-2)


# Задача 3. Апгрейд калькулятора

# def m(i,d):
#     if d == 'summ':
#         summ(i)
#     if d == 'max':
#         maxx(i)
#     if d == 'min':
#         minn(i)
#
# def summ(i):
#     p = 0
#     while i!=0:
#         p += i%10
#         i = i//10
#     print(p)
# def maxx(i):
#     m = i%10
#     while i!=0:
#         if i%10 > m:
#             m = i%10
#         i = i // 10
#     print(m)
# def minn(i):
#     m = i%10
#     while i != 0:
#         if i % 10 < m:
#             m = i % 10
#         i = i // 10
#     print(m)
#
# while True:
#     i = 2311989924#int(input('число = '))
#     d = 'max'#input('действие = ')
#     m(i,d)
#     break


# Задача 4. Число наоборот

# def reverse(c):
#     p = ''
#     while c != 0:
#         p += str(c%10)
#         c = c//10
#     print(p)
#
# n = [843287243,3432,904595,14512]
# for i in n:
#     reverse(i)


# Задача 5. Текстовый редактор

# def count_letters(c):
#     k = 0
#     n = 0
#     for i in c:
#         if i in s:
#             n += 1
#         if i in b:
#             k += 1
#     return k, n
#
# s = []
# b = []
# for i in range(10):
#     s.append(str(i))
# for i in range(65,123):
#     b.append(chr(i))
#
# print(count_letters('228b 49o8b2[pokj758j57j57j076j609k7j6 b8 2b'))


# Задача 6. Монетка
#
# def search(x,y):
#     if x in range(d1, d2) and y in range(v1,v2):
#         return 'принадлежит'
#     else:
#         return 'не принадлежит'
#
# d1 = 4
# d2 = 9
# v1 = 5
# v2 = 14
#
# x,y = 7, 12
#
# print(search(x,y))

from math import log
# Задача 7. Опять?

# def search(a,b):
#     try:
#         math.log(a-b)
#         return b
#     except ValueError:
#         return a
#
# a, b = -3,12
# print(search(a,b))


# Задача 8. НОД

# def searchd(a,b):
#     d = 0
#     for i in range(1,max(a,b)):
#         if a%i == 0 and b%i == 0:
#             d = i
#     return d
#
# def searchm(a,b):
#     while a!= b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
#
# a,b = 27,99
#
# print(searchm(a,b))

import random

# Задача 9. Недоделка

# def rock_paper_scissors():
#     while True:
#         c = input('камень, ножницы, бумага?:  ')
#         p = random.choice(['камень', 'ножницы', 'бумага'])
#         if c == p:
#             print(f'{c,p}ничья')
#             break
#         if (c == 'камень' and p == 'ножницы') or (c == 'бумага' and p == 'камень') or (c == 'ножницы' and p == 'бумага'):
#             print(f'{c,p}win')
#             break
#         else:
#             print(f'{c,p}lose')
#             break
#
#     mainMenu()
#
#
# def guess_the_number():
#     b = random.randint(1,5)
#     while True:
#         a = int(input('введите число от 1 до 5: '))
#         if a == b:
#             print('угадал')
#             break
#     mainMenu()
#
#
# def mainMenu():
#     while True:
#         v = int(input('Выберите игру: (1,2) '))
#         if v == 2:
#             guess_the_number()
#         elif v == 1:
#             rock_paper_scissors()
#         else:
#             break
#
# mainMenu()


# 13.6 Практическая работа

# Задача 1. Урок информатики 2

# def floatdot(a):
#     s = 0
#     if a>=10:
#         while a>=10:
#             a = a/10
#             s += 1
#     if a < 1:
#         while a < 1:
#             a = a*10
#             s -= 1
#     return a, s
#
# a = 0.0000241423414
# b,c = floatdot(a)
# print(f'x = {b} * 10 ** {c}')


# Задача 2. Функция максимума

# def search(a,b,c):
#     try:
#         math.log(a - b)
#         m = a
#     except ValueError:
#         m = b
#     try:
#         math.log(m - c)
#     except ValueError:
#         m = c
#     return m
#
#
# a, b, c = -3,12,1
# print(search(a,b,c))


# Задача 3. Число наоборот 2

# def plus(a,b):
#     a1 = ''
#     b1 = ''
#     c1 = ''
#     while a!=0:
#         a1 += str(a%10)
#         a = a//10
#     while b!=0:
#         b1 += str(b%10)
#         b = b//10
#     c = int(a1) + int(b1)
#     while c != 0:
#         c1 += str(c % 10)
#         c = c // 10
#     return c1
#
#
# a = 102#abs(int(input()))
# b = 123#abs(int(input()))
# print(plus(a,b))


# Задача 4. Урок информатики 3

# def mantis(a):
#     p = 0
#     while a >= 10:
#         p += 1
#         a = a/10
#     while a < 1:
#         p -= 1
#         a = a*10
#     return a, p
#
# a = 0.0000000001000215
# print(mantis(a))


# Задача 5. Недоделка 2
import  sys
#
# def count_n(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n = n // 10
#     return count
#
# def change(n, p):
#     count = count_n(n)
#     if count < 3 and p == 1:
#         print("В первом числе меньше трёх цифр.")
#         sys.exit()
#     if count < 4 and p == 2:
#         print("Во втором числе меньше четырёх цифр.")
#         sys.exit()
#     last_digit = n % 10
#     first_digit = n // 10 ** (count - 1)
#     between_digits = n % 10 ** (count - 1) // 10
#     n = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
#     return n
#
#
# first_n = int(input("Введите первое число: "))
# print('Изменённое первое число:', change(first_n, 1))
#
# second_n = int(input("Введите второе число: "))
# print('Изменённое второе число:', change(second_n, 2))
#
# print('Сумма чисел:', first_n + second_n)


# Задача 6. Маятник

# def count(a,o):
#     c = 1
#     while a > o:
#         a *= 0.916
#         c += 1
#     return  c
#
# a = 0.923 #int(input('a = '))
# o = 0.1 #int(input('o = '))
# print(count(a,o))


# Задача 7. Яйца

# import cmath
#
# def equasion(D):
#     A0 = 1
#     A1 = -3
#     A2 = -12
#     A3 = 10 - D
#     B1 = A1/A0
#     B2 = A2/A0
#     B3 = A3/A0
#     p = -1*B1**2/3 + B2
#     q = 2*B1**3/27 - B1*B2/3 + B3
#     Q = (p / 3) ** 3 + (q / 2) ** 2
#     print('p = ', p, '\nq = ', q, '\nQ = ', Q)
#     if q == 0:
#         F = cmath.pi / 2
#     if q < 0:
#         F = cmath.atan(-2 * cmath.sqrt(-Q) / q)
#     if q > 0:
#         F = cmath.atan(-2 * cmath.sqrt(-Q) / q) + cmath.pi
#
#     if Q < 0:
#         x1 = 2 * (-p / 3) ** 0.5 * cmath.cos(F / 3) - A1 / (3 * A0)
#         x1 = round(x1.real, 5)
#         x2 = 2 * (-p / 3) ** 0.5 * cmath.cos((F / 3) + 2 * cmath.pi / 3) - A1 / (3 * A0)
#         x2 = round(x2.real, 5)
#         x3 = 2 * (-p / 3) ** 0.5 * cmath.cos((F / 3) + 4 * cmath.pi / 3) - A1 / (3 * A0)
#         x3 = round(x3.real, 5)
#         print('\nx1 =', x1, '\nx2 =', x2, '\nx3 =', x3)
#     elif Q == 0:
#         x1 = 2 * (-q / 2) ** (1 / 3) - A1 / (3 * A0)
#         x2 = (-q / 2) ** (-1 / 3) - A1 / (3 * A0)
#         x3 = (-q / 2) ** (-1 / 3) - A1 / (3 * A0)
#         print('\nx1 =', x1, '\nx2 =', x2, '\nx3 =', x3)
#     elif Q > 0:
#         alfa = (-q / 2 + Q ** 0.5) ** (1 / 3)
#         beta = -abs((-q / 2 - Q ** 0.5) ** (1 / 3))
#         y1 = alfa + beta
#         y2 = complex(-((alfa + beta) / 2), (alfa - beta) / 2 * 3 ** 0.5)
#         y3 = complex(-((alfa + beta) / 2), -(alfa - beta) / 2 * 3 ** 0.5)
#         x1 = y1 - A1 / (3 * A0)
#         x1 = round(x1, 5)
#         x2 = y2 - A1 / (3 * A0)
#         x2 = round(x2.real, 5) + round(x2.imag, 5) * 1j
#         x3 = y3 - A1 / (3 * A0)
#         x3 = round(x3.real, 5) + round(x3.imag, 5) * 1j
#         print('\nalfa =', alfa, '\nbeta =', beta, '\n\nx1 =', x1, '\nx2 =', x2, '\nx3 =', x3)
#     for i in x1,x2,x3:
#         if i > 0 and i < 4:
#             print(f'глубина = {i}')
#
#
# D = float(input('введите D = '))
# equasion(D)


# Задача 8. Сумма ряда

# def series_sum(x,p):
#     s = 0
#     n = 1
#     while True:
#         step = x
#         fact = 1
#         if n%2 == 0:
#             m = 1
#         else:
#             m = -1
#         for i in range(1, 2*n+1):
#             fact = fact * i
#         for i in range(1, 2*n):
#             step = step * x
#         next = m * step/fact
#         s += next
#         if next < p:
#             break
#     return s
#
#
# p = 0.1
# x = 5
# n = 12
# fact = 1
# print(series_sum(x,p))


# Задача 9. Аннуитетный платёж

# def annuity(S,y,r):
#     i = r/100
#     K = (i*(1+i)**y)/((1+i)**y-1)
#     A = K*S
#     return A
#
# def rate_body(a,s,r):
#     p = s*r/12/100
#     b = a - p
#     return p, b
#
# def reannuity(s,y,r):
#     yn = 3  # На сколько лет увеличен срок?
#     print('На сколько лет увеличен срок?: 3')
#     rn = 2  # На сколько % увеличена ставка?
#     print('а сколько % увеличена ставка?: 2')
#     y += yn
#     r += rn
#     a = annuity(s,y,r)
#     return a, y, r
#
# def print_pay(y,a,s,r):
#     c = 0
#     while y != 1:
#         print(f'Остаток долга на начало периода: {s}')
#         p, b = rate_body(a,s,r)
#         print(f'Выплачено процентов: {p}')
#         print(f'Выплачено тела кредита: {b}')
#         s -= a
#         y -= 1
#         c += 1
#         if c == 3:
#             a, y, r = reannuity(s,y,r)
#
# s = 40*10**6  #Введите сумму кредита: 40e6
# y = 5  #На сколько лет выдан? 5
# r = 6  #Сколько процентов годовых? 6
#
# a = annuity(s,y,r)
# print_pay(y,a,s,r)


# 14.7 Практическая работа

# import platform
# import sys
#
# info = 'OS info is \n{}\nPython version is {} \n{}'.format(
#     platform.uname(),
#     sys.version,
#     platform.architecture(),
# )
# print(info)
#
# with open('os_info.txt', 'w', encoding='utf8') as file:
#     file.write(info)


# Задача 2. Сессия

# print("Введите первую точку")
# x1 = 10#float(input('X: '))
# y1 = 20#float(input('Y: '))
# print("Введите вторую точку")
# x2 = 15#float(input('X: '))
# y2 = 45#float(input('Y: '))
#
# x_diff = x1 - x2
# y_diff = y1 - y2
# k = y_diff / x_diff
# b = y2 - k * x2
#
# print("Уравнение прямой, проходящей через эти точки:")
# if b > 0:
#     print(print(f"y = {k} * x + {b}"))
# elif b < 0:
#     print(print(f"y = {k} * x {b}"))


# Задача 3. Сумма и разность

# def summa(n):
#     s = 0
#     while n !=0:
#         s += n%10
#         n = n//10
#     return s
#
# def amount(n):
#     a = len(str(n))
#     return a
#
# N =  500
# print(summa(N) - amount(N))


# Задача 4. Число наоборот 3

# def change(n):
#     # dlinadrobi = len(str((n - n//1)) - 2
#     d = round(n - n//1,2)
#     print(d)
#     n = int(n//1)
#     print(n)
#     sn = ''
#     sd = ''
#     while n != 0:
#         sn += str(n%10)
#         n = n//10
#     while d != 0:
#         d = d*10
#         sd += str(d%1)
#         d = d//10
#     print(sn)
#     print(sd)
#     sn = int(sn)
#     sd = float(sd)*10**(-len(sd))
#     print(sn)
#     print(sd)
#     print(sn+sd)
#     return sn+sd
#
# N = 102.12
# K = 123.34
# change(N)


# Задача 5. Наименьший делитель

# def minimum(n):
#     i = 2
#     while True:
#         if n%i == 0:
#             break
#         i+=1
#     return i
#
# n = 6
# print(minimum(n))


# Задача 6. Монетка 2

# x = 0.1
# y = -1
# c = math.sqrt(x**2+y**2)
# if c <= 1:
#     print('Монетка где-то рядом')
# else:
#     print('Монетки в области нет')

# Задача 7. Годы

# a = 1900
# b = 2100
# for i in range(a,b+1):
#     c = 0
#     if i//1000 == i%1000//100 == i%100//10 or i//1000 == i%1000//100 == i%10 or i//1000 == i%100//10 == i%10 or i%1000//100 == i%100//10 == i%10:
#         print(i)


# 15.6 Практическая работа (автотесты)

# n = 14
# N = []
# for i in range(n):
#     if i%2 == 1:
#         N.append(i)
# print(N)


# Задача 2. Турнир

# n = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# for i in range(0,len(n),2):
#     print(n[i])


# Задача 3. Клетки

# n = [1,3,2,5,2,4,7,8,1]
# for i, j in enumerate(n):
#     if j < i+1:
#         print(f'Эффективность {i+1} клетки: {j}')


# Задача 4. Видеокарты

# s = [3070, 2060, 3090, 3070, 3090]
# for j,i in enumerate(s):
#     if i == max(s):
#         s.remove(s[j])
# print(s)


# Задача 5. Кино

# n = 3
# s = ['бэмби','леон','бимуви','маяк','золушка','мария']
# loved = []
# for i in range(1, n+1):
#     f = input(f'введите название {i} фильма:  ')
#     if f in s:
#         loved.append(f)
#     else:
#         print('no')
#
# print(f'ваши фильмы:', ' '.join(loved))


# Задача 6. Анализ слова

# s = 'прившркркркет'
# su = []
# for i in s:
#     su.append(i)
#
# su = set(su)
# print(f'уникальных букв в слове {s}: {len(su)}')


# Задача 7. Контейнеры

# n = 4
# s = [165,165,163,162,161,159,159,143,132,132,100,99,99,99,98]
# sn = []
# p = 0
# c = 0
#
# k = int(input('введите массу нового контейнера:  '))
# try:
#     p = s.index(k)
# except:
#     ValueError
# try:
#     c = s.count(k)
# except:
#     ValueError
# print(p)
# print(c)
# if p != 0:
#     for i in range(p+c):
#         sn.append(s[i])
#     sn.insert(p+c,k)
#     for i in range(p+c,len(s)):
#         sn.append(s[i])
# elif p == 0:
#     for j, i in enumerate(s):
#         if k > i:
#             for n in range(j):
#                 sn.append(s[n])
#             sn.insert(j, k)
#             for m in range(j,len(s)):
#                 sn.append(s[m])
#             break
#     sn = s
#     sn.append(k)
#
# print(sn)


# Задача 8. Бегущие цифры

# def scroll(n,s,k):
#     new_index = []
#     if k > n:
#         k = k%n
#     k = n - k
#     for i in range(n):
#         if i + k < n:
#             new_index.append(s[i+k])
#         else:
#             ks = (k + i)%n
#             new_index.append(s[ks])
#     return new_index
#
# n = 7
# s = [1, 2, 3, 4, 5, 6, 7]
# k = 8
# print(scroll(n,s,k))


# Задача 9. Анализ слова 2

# def palindrom(s):
#     if len(s)%2 == 0:
#         d = 0
#     else:
#         d = 1
#     for i in range(len(s)//2 + d):
#         if s[i] != s[len(s)-i-1]:
#             p = 'не палиндром'
#             break
#         else:
#             p = 'палиндром'
#     return p
#
#
# c = 'мылоголым'
# n = 'унизилизину'
# q = 'тебе оно ебет'
# f = 'ароза упаланалапу азора'
# e = 'улыбок тебе дед мокар раком дед ебет кобылу'
# print(palindrom(c),palindrom(n),palindrom(q),palindrom(f),palindrom(e))


# Задача 10. Сортировка


# n = [4, 1, -3, 0, 10]
#
# while True:
#     c = 1
#     print(range(len(n)))
#     for j, i in enumerate(n):
#         print(j,i)
#         if j+1 in range(len(n)) and n[j] > n[j+1]:
#                  n[j], n[j+1] = n[j+1], n[j]
#                  c = 2
#     if c == 1:
#         break
#
# print(n)



# 16.6 Практическая работа

# Задача 1. Страшный код

# def first(a,b):
#     a.extend(b)
#     print(a.count(5))
#     for i in range(a.count(5)):
#         a.pop(a.index(5))
#     return a
#
# def second(a,c):
#     a.extend(c)
#     print(a.count(3))
#     return a
#
#
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# print(second(first(a,b),c))


# Задача 2. Шеренга

# a = [i for i in range(160, 177, 2)]
# b = [i for i in range(162, 181, 3)]
# a.extend(b)
# a.sort()
# print(a)


# Задача 3. Детали

# def price(shop,s):
#     k = 0
#     c = 0
#     for i in shop:
#         if i[0] == s:
#             k += 1
#             c += i[1]
#     return k,c
#
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# s = 'седло'
# print("k = %s, price = %s" %(price(shop,s)))


# Задача 4. Вечеринка

# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
#
# while True:
#     new = input('введите имя:  ')
#     if new == 'пора спать':
#         break
#     elif new not in guests and len(guests) < 6:
#         guests.append(new)
#     elif new in guests:
#         guests.remove(new)
#     print(guests)
# print('конец вечеринки')


# Задача 5. Песни

# def playlist_length(name,s):
#     for i in range(len(s)):
#         if name == s[i][0]:
#             t = s[i][1]
#     return t
#
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
#
# n = 3
# name1 = 'Halo'
# name2 = 'Enjoy the Silence'
# name3 = 'Clean'
# length = playlist_length(name3,violator_songs) + playlist_length(name2, violator_songs) + playlist_length(name1, violator_songs)
# print(round(length,2))


# Задача 6. Уникальные элементы

# l = [1, 2, 3]
# l2 = [2, 4, 6, 3, 3, 2, 1]
#
# l.extend(l2)
# l = list(set(l))
# print(l)


# Задача 7. Ролики

# k = [41,40,39,42]
# n = [42,41,40]
# c = 0
# for g, i in enumerate(k):
#     for h, j in enumerate(n):
#         if i == j:
#             c += 1
#             k.remove(i)
#             n.remove(j)
# print(c)


# Задача 8. Считалка

# l = [1, 2, 3, 4, 5]
# s = 1
# i = 0
# n = 7
# while len(l) > 1:
#     i = (i+n)%len(l)-1
#     if i == -1:
#         i = len(l)-1
#     l.pop(i)
#
# print(l)


# Задача 9. Друзья

# n = 3
# d = 1
# raspiski = []
# balance = [[i, 0] for i in range(1,n+1)]
# print(balance)
# for i in range(d):
#     k = int(input('komu:'))
#     o = int(input('ot kogo:'))
#     s = int(input('skolko:'))
#     raspiski.append([k,o,s])
#     print(raspiski)
#
# for i in balance:
#     print(i[0])
#     for j in raspiski:
#         if i[0] == j[0]:
#             i[1] += j[2]
#         if i[0] == j[1]:
#             i[1] -= j[2]
# print(balance)


# Задача 10. Симметричная последовательность

# def palindrom_check(chec):
#     if len(chec) % 2 == 0:
#         d = 0
#     else:
#         d = 1
#     for num in range(len(chec)//2 + d):
#         if chec[num] != p[len(p)-num-1]:
#             r = 'не палиндром'
#             break
#         else:
#             r = 'палиндром'
#     return r
#
#
# p = [1, 2, 3, 5, 7, 7, 7]
# n = len(p)
# chec = []
# chec.extend(p)
# v = 1
# dopolnenie = []
#
# for i in range(n-1):
#     if palindrom_check(chec) == 'палиндром':
#         break
#     else:
#         chec.pop(0)
#         v += 1
#
# for i in range(v-2, -1, -1):
#     dopolnenie.append(p[i])
#
# p.extend(dopolnenie)
# print(f'нужно цифр: {v-1}, новая последовательность: {p}')



# 17.7 Практическая работа

# Задача 1. Гласные буквы

# text = 'я бы никогда не купил шаурму без перца, это извращение и издевательство над традиционной культурой шаурмэйкинга'
# glas = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# glastext = [i for i in text if i in glas]
# print(glastext, '\n', len(glastext))


# Задача 2. Генерация

# n = 10
# strangelist = [(1 if i%2 == 0 else i%5) for i in range(n)]
# print(strangelist)


# Задача 3. Случайные соревнования

# l1 = [round(random.uniform(5,10),3) for _ in range(20)]
# l2 = [round(random.uniform(5,10),3) for _ in range(20)]
# l3 = [max(l1[i],l2[i]) for i in range(19)]
# print(f'{l1}\n {l2}\n {l3}\n')


# Задача 4. Тренируемся со срезами

# alphabet = 'abcdefg'
# print(f'1:{alphabet[:]}')
# print(f'1:{alphabet[::-1]}')
# print(f'1:{alphabet[0::2]}')
# print(f'1:{alphabet[1::2]}')
# print(f'1:{alphabet[:1]}')
# print(f'1:{alphabet[:-2:-1]}')
# print(f'1:{alphabet[3:4:]}')
# print(f'1:{alphabet[-3::1]}')
# print(f'1:{alphabet[3:5:]}')
# print(f'1:{alphabet[4:2:-1]}')


# Задача 5. Разворот

# str = 'hqwehrty'
# h_index = [j for j, i in enumerate(str) if i == 'h']
# print(f'Развёрнутая последовательность между первым и последним h: {str[h_index[1]:h_index[0]:-1]}')


# Задача 6. Сжатие списка

# n = 10
# lst = [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# lst.sort(key=lambda x: x==0)
# p = lst.count(0)
# for i in range(p):
#     lst.pop()
# print(lst)


# Задача 7. Двумерный список

# l = [[i, i+4, i+8] for i in range(1,5)]
# print(l)


# Задача 8. Развлечение

# def brosok(palki,br):
#     for j, i in enumerate(palki):
#         if j in range(br[0]-1, br[1]):
#             palki[j] = '.'
#     return palki
#
#
# n = 10
# k = 3
#
# a = [8,10]
# b = [2,5]
# c = [3,6]
# palki = ['1' for i in range(10)]
#
# print(''.join(brosok(palki,a)))
# print(''.join(brosok(palki,b)))
# print(''.join(brosok(palki,c)))


# Задача 9. Список списков

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# list = [k for i in nice_list for j in i for k in j]
# print(list)


# Задача 10. Шифр Цезаря

# def shifr(s,sdvig):
#     p = ''
#     for i in s:
#         if i == ' ':
#             p += chr(ord(i))
#         elif ord(i) + sdvig <= 1103:
#             p += chr(ord(i) + sdvig)
#         else:
#             p += chr(ord(i) + sdvig - 32)
#     return p
#
#
# s = 'это питон'
# sdvig = 3
# alf = [chr(i) for i in range(ord('а'), ord('а')+32)]
# print(shifr(s,sdvig))


# 18.6 Практическая работа

# Задача 1. Меню ресторана

# s = 'утиное филе;фланк-стейк;банановый пирог;плов'
# s = s.split(';')
# s = ', '.join(s,)
# print(s)


# Задача 2. Самое длинное слово

# s = 'я есть строка'
# s = s.split(' ')
# sl = max(s, key=len)
# print(sl)


# Задача 3. Файлы

# name = 'example.docx'
# sp = [chr(i) for i in range(30,65)]
# if name[0] in sp:
#     print('Ошибка: название начинается на один из специальных символов.')
# elif not name.endswith(('.docx', '.txt'), len(name) - 5, len(name)):
#     print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
# else:
#     print('Файл назван верно.')


# Задача 4. Заглавные буквы

# s = 'Кажется, я забыл выключить утюг.'
# s = s.split(' ')
# s = [i[0].upper()+i[1:] for i in s]
# s = ' '.join(s)
# print(s)


# Задача 5. Пароль

# while True:
#     parol = list(input('введите пароль: '))
#     if len([i for i in parol if i.isupper()]) > 0 and len([i for i in parol if i.isdigit()]) >= 3:
#         print('Это надёжный пароль!')
#         break


# Задача 6. Сжатие

# s = 'aaAAbbсaaaAAAa'
# sn = ''
# c = 1
# for j in range(len(s)-1):
#     print(j,' ',s[j],' ',s[j+1])
#     if s[j] == s[j+1] and j < len(s):
#         c += 1
#     elif s[j] != s[j+1] and j+1 < len(s):
#         sn += s[j] + str(c)
#         c = 1
#     if (s[j] == s[j+1] and j == len(s)-2) or (s[j] != s[j+1] and j == len(s)-2):
#         sn += s[j+1] + str(c)
#
# print(sn)


# Задача 7. IP-адрес 2

# while True:
#     er = 0
#     ip = input('vvedite IP:  ')
#     if ip.find(',') != -1:
#         print('Адрес — это четыре числа, разделённые .очками.')
#         er = 1
#     else:
#         ip = ip.split('.')
#         if len(ip) != 4:
#             print('Адрес — это 4етыре числа, разделённые точками.')
#             er = 1
#         for i in ip:
#             try:
#                 if int(i) > 255:
#                     print(i, 'превышает', 255)
#                     er = 1
#             except ValueError:
#                 print(f'{i} это не целое число.')
#                 er = 1
#     if er == 0:
#         print('IP-адрес корректен.')
#         break


# Задача 8. Бегущая строка

# def scroll(n,s,k):
#     new_index = []
#     k = n - k
#     for i in range(n):
#         if i + k < n:
#             new_index.append(s[i+k])
#         else:
#             ks = (k + i)%n
#             new_index.append(s[ks])
#     return new_index
#
# s = list('abcde')
# s2 = list('deabc')
# print(s,s2)
# n = len(s)
# if len(s) == len(s2):
#     for k in range(n):
#         if (scroll(n,s,k)) == s2:
#             print(f'Первая строка получается из второй со сдвигом {k+1}')
# else:
#     print('строки разной длины')


# Задача 9. Сообщение

# def shifr(s):
#     a = ord('А')
#     ya = ord('я')
#     s1 = ''
#     for i in s:
#         prepinanie = ''
#         for j in range((len(i) - 1), -1, -1):
#             if ord(i[j]) in range(a, ya):
#                 s1 += i[j]
#             else:
#                 prepinanie = i[j]
#         s1 += prepinanie + ' '
#     return s1
#
# s = 'Это задание очень! простое.'
# s = s.split()
# print(shifr(s))


# Задача 10. Истина

# s = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
#
# def shifr(s,sdvig):
#     LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     p = ''
#     p1 = ''
#     for i in s:
#         if i in LETTERS:
#             num = LETTERS.find(i)
#             p += LETTERS[num - sdvig]
#         else:
#             p += i
#     p = p.split()
#     drop = 3
#     for i in p:
#         word = ''
#         for j in range(len(i)):
#             word += (i[j - drop % len(i)])
#         if word.endswith('/'):
#             drop += 1
#         p1 += word + ' '
#     p1 = p1.replace('/','\n')
#     return p1
#
# sdvig = 1
# print(shifr(s,sdvig))



# 19.6 Практическая работа

# Задача 1. Песни 2

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
#     }
# n = 3
# lenght = 0
# pesni = ['Halo', 'Enjoy the Silence', 'Clean']
# for j, i in enumerate(violator_songs.keys()):
#     if i in pesni:
#         lenght += violator_songs[i]
#
# print(lenght)


# Задача 2. География

# data = {}
# s = 'Россия Москва Петербург Новгород'
# country,*cities = s.split()
# s = s.split()
# print(s)
# #data.update({country:cities})
# for country,cities in data.items():
#     gorod = input('введите город:  ')
#     if gorod in cities:
#         print(f'Город {gorod} расположен в стране {country}.')


# Задача 3. Криптовалюта

# data = {
#     "address": "0x544444444444",
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#     },
#     "count_txs": 2,
#     "tokens": [
#         {
#             "fst_token_info": {
#                 "address": "0x44444",
#                 "name": "fdf",
#                 "decimals": 0,
#                 "symbol": "dsfdsf",
#                 "total_supply": "3228562189",
#                 "owner": "0x44444",
#                 "last_updated": 1519022607901,
#                 "issuances_count": 0,
#                 "holders_count": 137528,
#                 "price": False
#             },
#             "balance": 5000,
#             "totalIn": 0,
#             "total_out": 0
#         },
#         {
#             "sec_token_info": {
#                 "address": "0x44444",
#                 "name": "ggg",
#                 "decimals": "2",
#                 "symbol": "fff",
#                 "total_supply": "250000000000",
#                 "owner": "0x44444",
#                 "last_updated": 1520452201,
#                 "issuances_count": 0,
#                 "holders_count": 20707,
#                 "price": False
#             },
#             "balance": 500,
#             "totalIn": 0,
#             "total_out": 0
#         }
#     ]
# }
#
# def printing(data):
#     print(data.keys())
#     print(data.values())
#
# def changelvl1(data):
#     ETH = data.get('ETH')
#     ETH.update({'total_diff': 100})
#     data.update({'ETH': ETH})
#     return data
#
# def change_valuelvl2(data):
#     tokens = data.get("tokens")
#     first = tokens[0]
#     fst = first.get('fst_token_info')
#     fst.update({'name': 'doge'})
#     first.update({"fst_token_info": fst})
#     data.update({"tokens": first})
#     return data
#
# def delete(data,totalout):
#     tokens = data.get("tokens")
#     total = tokens[0]
#     print(total)
#     totalout = total.pop(totalout)
#     ETH = data.get('ETH')
#     ETH.update({'total_out': totalout})
#     data.update({'ETH': ETH})
#     return data
#
# def change_keylvl2(data,k1,k2):
#     tokens = data.get("tokens")
#     second = tokens[1]
#     sec = second.get('sec_token_info')
#     value = sec[k1]
#     sec.pop(k1)
#     sec.update({k2: value})
#     second.update({'sec_token_info' : sec})
#     tokens[1] = second
#     data.update({"tokens": tokens})
#     return  data
#
# printing(data)
# changelvl1(data)
# change_valuelvl2(data)
# delete(data,'total_out')
# change_keylvl2(data,'price','total_price')


# Задача 4. Товары

# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
#
# for k in store:
#     # print(k, '->', store[k])
#     quant = 0
#     cost = 0
#     for k1 in store[k]:
#         quant += k1['quantity']
#         cost += k1['quantity']*k1['price']
#     print(f'{list(goods.keys())[list(goods.values()).index(k)]}: quant = {quant}, total cost = {cost}')


# Задача 5. Гистограмма частоты 2

# orig = {' ': 2,'-' : 1,'З' : 1,'а' : 2,'д' : 1,'е' : 1,'и' : 1,'н' : 2,'о' : 3,'п' : 1,'с' : 2,'т' : 2,'ч' : 1,'ь' : 1}
# keys = set(list(orig.values()))
# invert = dict.fromkeys(keys, '')
# print(invert)
# for i in range(len(orig)):
#     key = list(orig.values())[i]
#     value = list(orig.keys())[i]
#     invert[key] += value
# for i in invert:
#     invert[i] = list(invert[i])
# print(invert)


# Задача 6. Словарь синонимов

# n = 1
# dictionary_synonim = {}
#
# for i in range(n):
#     pair = input('пара:  ').split()
#     dictionary_synonim.update({pair[0]: pair[len(pair) - 1]})
#     print(dictionary_synonim)
#
# while True:
#     p = input('пара:  ')
#     if p in list(dictionary_synonim.keys()):
#         print(f'Синоним: {dictionary_synonim[p]}')
#     elif p in list(dictionary_synonim.values()):
#         print(f'Синоним: {list(dictionary_synonim.keys())[list(dictionary_synonim.values()).index(p)]}')
#     else:
#         print('такого синонима нет')
#         break


# Задача 7. Пицца

# n = 3
# dict_orders = {}
# for i in range(n):
#     order = input('заказ:  ').split()
#     name = order[0]
#     choice = order[1]
#     amount = int(order[2])
#     dictorder = dict.fromkeys({choice},amount)
#     if name not in list(dict_orders.keys()):
#         dict_orders.update({name:dictorder})
#     elif name in list(dict_orders.keys()) and choice not in list(dict_orders[name].keys()):
#         dict_orders[name].update(dictorder)
#     elif name in list(dict_orders.keys()) and choice in list(dict_orders[name].keys()):
#         amount += dict_orders[name][choice]
#         dictorder = dict.fromkeys({choice}, amount)
#         dict_orders[name].update(dictorder)
#     print(dict_orders)
#
# dict_ordersss = dict(sorted(dict_orders.items(), key=lambda x: x[0]))
#
# print(dict_ordersss)


# Задача 8. Угадай число

# n = int(input('введите максимальное число:  '))
# z = int(input('загадайте число число:  '))
# tray = []
#
# while True:
#     ask = input('сдаешься? ')
#     if ask == 'Помогите!':
#         break
#     while len(tray) < random.randint(0,n//2):
#         new = random.randint(1, n)
#         if new not in tray:
#             tray.append(new)
#     tray = list(sorted(tray))
#     print(f'Нужное число есть среди вот этих чисел: ',  tray)
#     if z in tray:
#         print('да')
#         r = random.randint(0, len(tray)-1)
#         tr = tray[r]
#         tray.clear()
#         tray.append(tr)
#     else:
#         print('нет')
#         tray = [i for i in range(n) if i not in tray]
#
# print(f'Артём мог загадать следующие числа: {random.randint(1, z-1)} {z} {random.randint(z+1, n)}')


# Задача 9. Родословная

# def prokidka(proroditel,lvl):
#     lvl += 1
#     for j in drevo[proroditel]:
#         drevo_grade[j] += lvl
#         if j in list_roditeli:
#             prokidka(j,lvl)
#
#
# n = 8
# drevo = {}
# drevo_grade = {}
# list_potomki = []
# list_roditeli = []
# lvl = 0
# with open('C:\X\GitHub\Basic_courses/rodoslov.txt') as f:
#     lines = f.readlines()
#
# for i in lines:
#     pair = i.split()
#     rod = pair[1]
#     pot = pair[0]
#     drevo_grade.update({rod : 0})
#     drevo_grade.update({pot : 0})
#     list_potomki.append(pot)
#     list_roditeli.append(rod)
#     if rod not in list(drevo.keys()):
#         drevo.update({rod:[pot]})
#     else:
#         drevo[rod].append(pot)
#     # print(drevo)
# print(drevo_grade)
#
# for i in list(drevo_grade.keys()):
#     if i not in list_potomki:
#         proroditel = i
#
# prokidka(proroditel,lvl)
# drevo_gradesort = dict(sorted(drevo_grade.items(), key=lambda x: x[0]))
# print(drevo_gradesort)


# Задача 10. Снова палиндром

# import itertools
#
# def palindrom_check(chec):
#     if len(chec) % 2 == 0:
#         d = 0
#     else:
#         d = 1
#     for num in range(len(chec)//2 + d):
#         if chec[num] != chec[len(chec)-num-1]:
#             r = 'не палиндром'
#             break
#         else:
#             r = 'палиндром'
#     return r
#
# def iterations(s):
#     s = list(s)
#     r = 'не палиндром'
#     for i in itertools.permutations(s):
#         combo = "".join(i)
#         if palindrom_check(combo) == 'палиндром':
#             r = 'палиндром'
#             break
#     return  r
#
# s = 'aabbc'
# print(iterations(s))



# 20.8 Практическая работа

# Задача 1. Ревью кода

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     return lst, len(string)
#
#
# pairs = [(i, students[i]['age']) for i in students]
# print(pairs)
#
#
# my_lst, l = f(students)[0], f(students)[1]
# print(my_lst, l)


# Задача 2. Универсальная программа 2

# def crypto(iter):
#     return [i for j, i in enumerate(iter) if prost(j) is True]
#
# def prost(j):
#     if j in [0,1]:
#         return True
#     d = 2
#     while j%d != 0:
#         d += 1
#     return d == j
#
#
# print(crypto('О Дивный Новый мир!'))


# Задача 3. Функция

# def slicer(cort,n):
#     if cort.count(n) == 0:
#         cort = ()
#     elif cort.count(n) >= 2:
#         cort = cort[cort.index(n):cort.index(n,cort.index(n)+1,len(cort))]
#     else:
#         cort = cort[cort.index(n):]
#     return cort
#
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 3))


# Задача 4. Игроки

# players = {
#
#     ("Ivan", "Volkin"): (10, 5, 13),
#
#     ("Bob", "Robbin"): (7, 5, 14),
#
#     ("Rob", "Bobbin"): (12, 8, 2)
#
# }
#
# p = [(list(players.keys())[i]+list(players.values())[i]) for i in range(len(players))]
# print(p)


# Задача 5. Одна семья

# family = {
#     ('Сидоров', 'Никита') : 32,
#     ('Сидорова', 'Алина') : 34,
#     ('Сидоров', 'Павел') : 10,
#     ('Соин', 'Никита') : 23,
#     ('Сурова', 'Ксения') : 24
# }
#
# p = 'суров'
# p = p.lower()
# for j,i in enumerate(list(family.keys())):
#     if i[0].lower() == p or i[0][:len(i[0])-1].lower() == p or i[0].lower() == p[:len(p)-1]:
#         print(i,family[i])


# Задача 6. По парам

# p = [random.randint(0,10) for i in range(10)]
# n = []
# i = 0
# for num in range(len(p)//2):
#     n.append((p[i],p[i+1]))
#     i = i+1
# print(n)


# Задача 7. Функция сортировки

# def tpl_sort(*args):
#     for i in args:
#         if i < 0:
#             return args
#     a = tuple(set(args))
#     return a
#
# print(tpl_sort(6, 3, -1, 8, 4, 10, 5))


# Задача 8. Контакты 3

# kontacts = {('Иван', 'Сидоров'): 888,('Алиса', 'Петрова'): 999}
#
# def one():
#     name = input('имя: ')
#     surname = input('фамилия?  ')
#     number = int(input('номер?  '))
#     kontacts.update({(name,surname):number})
#     return kontacts
#
# def two():
#     p = input('введите нужную фамилию:  ').lower()
#     for j,i in enumerate(list(kontacts.keys())):
#         if i[1].lower() == p or i[1][:len(i[1])-1].lower() == p or i[1].lower() == p[:len(p)-1]:
#             print(i,kontacts[i])
#
#
# while True:
#     d = input('Введите номер действия: \n  1. Добавить контакт \n  2. Найти человека \n:')
#     if d == '1':
#         print(one())
#     if d == '2':
#         two()


# Задача 9. Протокол соревнований

# def zipi(o,t):
#     return [(o[i], t[i]) for i in range(len(one))]
#
# one = 'abcd'
# two =  (10, 20, 30, 40)
#
# print(zipi(one,two))



# 21.6 Практическая работа

# Задача 1. Challenge 2

# def recurs(n,num):
#     print(n)
#     if n < num:
#         n += 1
#         recurs(n,num)
#
# n = 0
# num = 10
# recurs(n,num)


# Задача 2. Свой zip 2

# def zipi(o,t):
#     return [(o[i], t[i]) for i in range(len(one))]
#
# one = 'abcd'
# two =  (10, 20, 30, 40)
#
# print(zipi(one,two))


# Задача 3. Ряд Фибоначчи

# def fibonacci(one,two,n,p):
#     n += 1
#     if n < p:
#         one, two = two, one + two
#         fibonacci(one,two,n,p)
#     if n == p:
#         print(two)
#
#
# one = 0
# two = 1
# n = 0
# p = 10
# fibonacci(one,two,n,p)


# Задача 4. Поиск элемента 2

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# def deeper(a,key):
#     for k in list(a.keys()):
#         if k == key:
#             print('конец: ', a[k])
#             break
#         if type(a[k]) == dict:
#             deeper(a[k],key)
#
# a = site
# key = 'title'
# deeper(a,key)


# Задача 5. Ускоряем работу функции

# def calculating_math_func(data):
#     result = 1
#     if data not in list(factorial.keys()):
#         for index in range(1, data + 1):
#             result *= index
#         factorial.update({data:result})
#     else:
#         result = factorial[data]
#     result /= data ** 3
#     result = result ** 10
#     return result
#
# factorial = {}


# Задача 6. Глубокое копирование


# def sytic(name):
#     site = {
#         'html': {
#             'head': {
#                 'title': f'Куплю/продам {name} недорого'
#             },
#             'body': {
#                 'h2': f'У нас самая низкая цена на {name}',
#                 'div': 'Купить',
#                 'p': 'Продать'
#             }
#         }
#     }
#     return site
#
# n = int(input('сколько сайтов нужно?  '))
# for i in range(n):
#     name = input('введите название первого сайта:  ')
#     print(sytic(name))


# Задача 7. Продвинутая функция sum

# def sum2(lst,s = 0):
#     for i in lst:
#         try:
#             s += i
#         except TypeError:
#             s = sum2(i, s)
#     return s
#
# print(sum2([[1, [6], [3]], [[[4]], 5]]))


# Задача 8. Список списков 2

# def nice(lst,s = []):
#     for i in lst:
#         print(i)
#         if type(i) != list:
#             s.append(i)
#         else:
#             d = nice(i, s)
#             s.append(d)
#         print(s)
#     for j, e in enumerate(s):
#         if type(e) == list:
#             s.pop(j)
#     return s
#
# print(nice([[1, 2, [3, 4], [[5, 6, 7], [[8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]]]))



# 22.6 Практическая работа

# Задача 1. Сумма чисел 2

# f = open('text.txt')
# s = 0
# for line in f:
#     l = line.split()
#     s += int(l[0])
# d = open('answer.txt', 'a')
# d.write(str(s))
# print('Содержимое файла answer.txt \n', open('answer.txt').read())


# Задача 2. Дзен Пайтона

# for i in reversed(open('text.txt').read().split('\n')):
#     print(i)


# Задача 3. Дзен Пайтона 2
# s = 0
# sl = 0
# bukva = 0
# redkiy_slovar = {}
# for i in reversed(open('text.txt').read().split('\n')):
#     s += 1
#     str = i.split()
#     for j in str:
#         sl += 1
#         slovo = list(j)
#         for b in slovo:
#             bukva += 1
#             if b not in redkiy_slovar:
#                 redkiy_slovar.update({b:0})
#             else:
#                 redkiy_slovar[b] += 1
# most = max(list(redkiy_slovar.values()))
# print(list(redkiy_slovar.items())[list(redkiy_slovar.values()).index(most)])
# print(s,sl,bukva)

import os

# Задача 4. Файлы и папки

# def rec_file(path, f = 0, cat = 0, size = 0):
#     pa, dirs, files = next(os.walk(path))
#     for i in files:
#         f += 1
#         fp = os.path.join(path, i)
#         size += os.path.getsize(fp)
#     for j in dirs:
#         dp = os.path.join(path, j)
#         cat += 1
#         f,cat,size = rec_file(dp,f,cat,size)
#     return f,cat,size
#
# home = 'C:\X\GitHub'
# f,cat,size = rec_file('C:\X\GitHub')
# print(f'Размер каталога (в Кб): {f}\nКоличество подкаталогов: {cat}\nКоличество файлов: {size}')


# Задача 5. Сохранение

# str = 'testiruyem' # input('введите строку:  ')
# path = 'C: X GitHub'.split()
# p = ''
# for i in path:
#     p += os.path.join(i) + "\\"
# file_name = 'my_document' + '.txt'
# f = open(os.path.join(p,file_name),'w')
# f.write(str)
# f = open(os.path.join(p,file_name))
# print(f.read())


# Задача 6. Паранойя

# def shifr(line, sdvig, p = '', LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     for i in line:
#         if i in LETTERS:
#             num = LETTERS.find(i)
#             if num + sdvig <= len(LETTERS):
#                 p += LETTERS[num + sdvig]
#             else:
#                 p += LETTERS[num + sdvig - len(LETTERS)]
#         else:
#             p += i
#     return p
#
# f = open('text.txt')
# r = open('cipher_text.txt','w')
# sdvig = 1
# for i in f:
#     newline = shifr(i, sdvig)
#     sdvig += 1
#     r.write(newline)
# r.close()
# r = open('cipher_text.txt')
# print(r.read())


# Задача 7. Турнир

# edge = int(open('first_tour.txt').read()[0:2])
# f = open('first_tour.txt')
# w = open('second_tour.txt', 'w')
# for i in f:
#     line = i.split()
#     if len(line) == 3:
#         if int(line[2]) > edge:
#             w.write(f'{line[1][0]}. {line[0]} {line[2]} \n')
#
# w = open('second_tour.txt','r')
# print(w.read())


# Задача 8. Частотный анализ

# def unicue(text,unicue_dict = {}, part_dict = {}, LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     f = open(text).read()
#     for i in f:
#         if i in LETTERS:
#             if i.lower() not in unicue_dict.keys():
#                 unicue_dict.update({i.lower():1})
#             else:
#                 unicue_dict[i] += 1
#     s = sum(unicue_dict.values())
#     print(s)
#     for j in range(len(unicue_dict)):
#         part_dict.update({list(unicue_dict.keys())[j]:round(list(unicue_dict.values())[j]/s, 3)})
#     part_dict_s = sorted(part_dict.items(), key=lambda x:(-x[1], x[0]))
#     return part_dict_s
#
# name = 'text.txt'
# print(unicue(name))



# 23.6 Практическая работа

# Задача 1. Имена 2

# s = 0
# with open('people.txt','r') as p:
#     for j,i in enumerate(p):
#         try:
#             s += len(i)
#             if len(i) < 3:
#                 raise TabError
#         except TabError:
#             print(f'длина строки №{j} меньше 3')
# print(s)


# Задача 2. Координаты

import random

#
#
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return x / y
#
#
# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)
#     return y / x
#
#
#
# file = open('coordinates.txt', 'r')
# for line in file:
#     nums_list = line.split()
#     res1 = f(int(nums_list[0]), int(nums_list[1]))
#     res2 = f2(int(nums_list[0]), int(nums_list[1]))
#
#     number = random.randint(0, 100)
#     file_2 = open('result.txt', 'w')
#     my_list = sorted([res1, res2, number])
#     file_2.write(my_list)
#
# file.close()
# file_2.close()


# Задача 3. Счастливое число

# def filesum(name,s = 0):
#     f = open('out_file.txt', 'r')
#     s = int(f.read())
#     print(s)
#     return s
#
#
# while True:
#     r = random.randint(0,13)
#     print(r,'= r')
#     if r == 4:
#         break
#     d = filesum('out_file.txt')
#     if d < 777:
#         file = open('out_file.txt', 'w')
#         new = int(input('введите новое число:  ')) + d
#         file.write(str(new))
#         file.close()
#     else:
#         break
#
# file = open('out_file.txt', 'w')
# file.write('0')
# file.close()


# Задача 4. Регистрация

# def letters(name, let = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     for i in name:
#         if i not in let:
#             return 0
#     return 1
#
# def emai(mail):
#     if '@' not in mail or '.' not in mail:
#         return False
#     return True
#
# file = open('out_file.txt', 'r')
# filefalse = open('filefalse', 'w')
# filetrue = open('filetrue', 'w')
#
# for i in file:
#     try:
#         if len(i.split()) != 3:
#             raise IndexError
#         elif letters(i.split()[0]) == 0:
#             raise NameError
#         elif emai(list(i.split()[1])) is False:
#             raise SyntaxError
#         elif int(i.split()[2]) in range(10,100):
#             raise ValueError
#         else:
#             filetrue.write(i)
#     except IndexError:
#         filefalse.write(f'{i[:-1]} НЕ присутствуют все три поля: IndexError.\n')
#     except NameError:
#         filefalse.write(f'{i[:-1]} Поле имени содержит НЕ только буквы: NameError.\n')
#     except SyntaxError:
#         filefalse.write(f'{i[:-1]} Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.\n')
#     except ValueError:
#         filefalse.write(f'{i[:-1]} Поле «Возраст» НЕ является числом от 10 до 99: ValueError.\n')


# Задача 5. Текстовый калькулятор

# def calc(name, s = 0):
#     for i in open(name, 'r'):
#         s += calculation(i.split())
#     return s
#
#
# def calculation(str,r = 0):
#     try:
#         if str[1] == '+':
#             r = int(str[0]) + int(str[2])
#         elif str[1] == '*':
#             r = int(str[0]) * int(str[2])
#         elif str[1] == '/':
#             r = int(str[0]) / int(str[2])
#         elif str[1] == '-':
#             r = int(str[0]) - int(str[2])
#         else:
#             raise ValueError
#     except ValueError:
#         st = ' '.join(str)
#         d = input(f'Программа пытается выполнить {st}. Хотите исправить ошибку?\n')
#         if d == 'да':
#             z = input('Введите новую строку: ')
#             r = calculation(z.split())
#     return r
#
#
# print(f'summa = {calc("calc.txt")}')


# 24.6 Практическая работа

# class Family:
#     surname = 'Common'
#     money = 10000
#     have_home = False
#
#     def info(self):
#         print(
#             f'Name {self.surname}\nmoney {self.money}\nHome {self.have_home}'
#         )
#
#     def earn(self, amount):
#         self.money += amount
#         print(f'Earned {amount}, current {self.money}')
#
#     def by(self,house_pricce,discount = 0):
#         house_pricce -= house_pricce*discount/100
#         if self.money >= house_pricce:
#             self.money -= house_pricce
#             self.have_home = True
#             print(f'Congrats! Money: {self.money}')
#         else:
#             print('No')
#
# my_famili = Family()
# my_famili.info()
# my_famili.by(11100,9)


# class Employee:
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
#     def print_info(self):
#         print(
#             f'Name {self.name}, salary {self.salary}'
#         )
#
# emp1 = Employee('obo',50)
# emp1.print_info()


# class Potato:
#     states = {0:'ничего', 1:'рост', 2:'клубень'}
#
#     def __init__(self,index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 2:
#             self.state += 1
#         self.print_state()
#
#     def print_state(self):
#         print(
#             f'Pot {self.index} is now {Potato.states[self.state]}'
#         )
#
# class Potato_garden:
#     def __init__(self,count):
#         self.potatoes = [Potato(i) for i in range(1,count + 1)]
#
#     def grow_all(self):
#         print('it grows')
#         for i in self.potatoes:
#             i.grow()
#
#     def all_growed_up(self):
#         for i in self.potatoes:
#             if i.state != 2:
#                 print('не созрела')
#                 break
#         else:
#             print('все созрело')

# from garden import *
# garden = Potato_garden(6)
# garden.all_growed_up()
# for i in range(2):
#     garden.grow_all()
#     garden.all_growed_up()


# Задача 1. Драка

# class Warrior:
#
#     def __init__(self):
#         self.hp = 100
#         self.name = 'Voin'
#
#     def get_hp(self):
#         return self.hp
#
#     def GetName(self):
#         for i, j in globals().items():
#             if j is self:
#                 return i
#
#     def get_hit(self):
#         self.hp -= 20
#         print(f'{self.GetName()} получил удар и потерял 20 здоровья, теперь его хп = {self.hp}')
#
# war1 = Warrior()
# war2 = Warrior()
#
# while war2.get_hp() > 0 and war1.get_hp() > 0:
#     r = random.randint(1,2)
#     if r == 1:
#         war1.get_hit()
#     else:
#         war2.get_hit()


# Задача 2. Студенты

# class Student:
#
#     def __init__(self,name,group,grades):
#         self.name = name
#         self.group = group
#         self.grades = grades
#
#     def print_info(self):
#         print('{} {} {}'.format(self.name,self.group,self.grades),end=', ')
#
#
# g = [Student('Bob3', '2a', 0),
# Student('Aob3', '2a', 1),
# Student('Bob1', '2a', 2),
# Student('Dob1', '2a', 3),
# Student('Bob8', '2a', 4)]
#
# print(g)
# g.sort(key=lambda x : x.name)
# for i in g:
#     i.print_info()


# Задача 3. Круг

# class Round:
#
#     def __init__(self, r, x0 = 0, y0 = 0):
#         self.x0 = x0
#         self.y0 = y0
#         self.r = r
#
#     def square(self):
#         return math.pi*self.r**2
#
#     def lenght(self):
#         return 2*math.pi*self.r
#
#     def grow(self):
#         self.r = 2*self.r
#
#     def intersection(self,x1,y1,r2):
#         if abs(x1) + r2 >= self.r + self.x0 or abs(y1) + r2 >= self.r + self.y0:
#             return True
#         else:
#             return False
#
# krug = Round(3)
# print(krug.lenght())
# print(krug.square())
# print(krug.intersection(0.5,0.5,2.5))


# Задача 4. Отцы, матери и дети

# class Parent:
#
#     def __init__(self,name,old):
#         self.name = name
#         self.old = old
#         self.children = [Children('Mike',random.randint(1,self.old - 16)) for i in range(4)]
#
#     def child_info(self):
#         for i in self.children:
#             print('{} {} {} {}'.format(i.name,i.cold,i.easy,i.ishungry))
#
#     def make_easy(self,cname):
#         for i in self.children:
#             if i.name == cname:
#                 i.easy = True
#
#     def feed(self,cname):
#         for i in self.children:
#             if i.name == cname:
#                 i.ishungry = False
#
# class Children:
#
#     def __init__(self,name,cold):
#         self.name = name
#         self.cold = cold
#         self.easy = False
#         self.ishungry = True
#
# dad = Parent('Matt',28)
# dad.child_info()
# dad.make_easy('Mike')
# dad.feed('Mike')
# dad.child_info()


# Задача 5. Весёлая ферма 2

# class Potato:
#
#     states = {0:'ничего', 1:'росток', 2:'клубень'}
#
#     def __init__(self,index):
#         self.index = index
#         self.state = 0
#         self.sornyak = True
#
#     def grow(self):
#         if self.state < 2:
#             self.state += 1
#         # self.print_state()
#
#     def print_state(self):
#         print(
#             f'Potato {self.index} is now {Potato.states[self.state]}. Sornyak {self.sornyak}'
#         )
#
#     def propolka(self):
#         self.sornyak = False
#
# class Potato_garden:
#
#     def __init__(self,count):
#         self.potatoes = [Potato(i) for i in range(1,count + 1)]
#
#     def grow_all(self):
#         print('it grows')
#         for i in self.potatoes:
#             i.grow()
#
#     def print_info_potato_garden(self):
#         for i in self.potatoes:
#             i.print_state()
#
#     def all_growed_up(self):
#         for i in self.potatoes:
#             if i.state != 2:
#                 print('не созрела')
#                 break
#         else:
#             print('все созрело')
#
#     def polka(self):
#         for i in self.potatoes:
#             i.propolka()
#
#     def pick_up(self, s = 0):
#         for i in self.potatoes:
#             s+=1
#         return s
#
# class Gardener:
#
#     def __init__(self,name):
#         self.name = name
#         self.gryadka = Potato_garden(5)
#
#     def popropoloty(self):
#         self.gryadka.polka()
#
#     def collecting(self):
#         print(f'Собрано {self.gryadka.pick_up()} картошек')
#
# s = Gardener('Mike')
# s.gryadka.print_info_potato_garden()
# s.popropoloty()
# s.gryadka.grow_all()
# s.gryadka.grow_all()
# s.gryadka.print_info_potato_garden()
# s.collecting()


# Задача 6. Магия

# class Water:
#     def __str__(self):
#         return 'water'
#
#     def __add__(self, other):
#         if isinstance(other,Air):
#             return Shtorm()
#         elif isinstance(other,Fire):
#             return Par()
#         elif isinstance(other,Earth):
#             return Dirt()
#         else:
#             return None
#
#
# class Fire:
#     def __init__(self):
#         self.name = 'fire'
#
#     def __add__(self, other):
#         if other.name == 'earth':
#             return Magma()
#         elif other.name == 'water':
#             return Par()
#         elif other.name == 'air':
#             return Lightning()
#
#
# class Earth:
#     def __init__(self):
#         self.name = 'earth'
#
#     def __add__(self, other):
#         if other.name == 'fire':
#             return Magma()
#         elif other.name == 'water':
#             return Dirt()
#         elif other.name == 'air':
#             return Pyl()
#
#
# class Air:
#     def __init__(self):
#         self.name = 'air'
#
#     def __add__(self, other):
#         if other.name == 'fire':
#             return Lightning()
#         elif other.name == 'water':
#             return Shtorm()
#         elif other.name == 'earth':
#             return Pyl()
#
#
# class Shtorm:
#     def __str__(self):
#         return 'storm'
#
#
# class Par:
#     def __str__(self):
#         return 'par'
#
#
# class Dirt:
#     def __init__(self):
#         self.name = 'dirt'
#
#
# class Lightning:
#     def __init__(self):
#         self.name = 'lightning'
#
#
# class Pyl:
#     def __init__(self):
#         self.name = 'pyl'
#
#
# class Magma:
#     def __init__(self):
#         self.name = 'magma'
#
#
# c = Water() + 5
# print(c)



# Задача на симметричное деление множества точек по вертикальной оси - алгоритмы

# def pair_check(m):
#     for i in range(0, len(m), 2):
#         if m[i + 1][1] != m[i][1]:
#             print('ошибка пар')
#             return False
#     return True
#
# def range_check(m):
#     c = abs(m[0][0] - m[1][0])/2 + min(m[0][0],m[1][0])
#     print(c)
#     for i in range(2, len(m), 2):
#         x1 = m[i][0]
#         x2 = m[i+1][0]
#         d = abs(x1 - x2)/2 + min(x1,x2)
#         print(f'проверяем: d={d},при x1={x1},x2={x2}. =? c={c}')
#         if d != c:  # уточнить проверку расстояния
#             print(f'ошибка расстояний: d={d},x1={x1},x2={x2} != c={c}')
#             return False
#     return True
#
# m = [[1,0],[8,0],[6,1],[3,1],[2,3],[7,3]]
# m = sorted(m,key=lambda x : -x[1])
# print(m)
# if pair_check(m) == True and range_check(m) == True:
#     print('множество можно разделить вертикалью симметрично')
# else:
#     print('множество нельзя разделить вертикалью симметрично')


# Задача 7. Совместное проживание

# class Man:
#     def __init__(self):
#         self.name = 'Artyom'
#         self.nohungry = 50
#         self.home = Home()
#
#     def eat(self):
#         self.nohungry += 10
#         if man.home.food > 0:
#             man.home.food -= 1
#         else:
#             man.home.food -= 1
#             man.home.no_food = True
#
#     def work(self):
#         self.nohungry -= 10
#         man.home.money += 10
#
#     def play(self):
#         self.nohungry -= 5
#
#     def shop(self):
#         man.home.food += 10
#         man.home.money -= 10
#
#     def live(self,d=0):
#         while True:
#             k = doit()
#             if man.nohungry < 20:
#                 man.eat()
#             elif man.home.food < 10:
#                 man.shop()
#             elif man.home.money < 50:
#                 man.work()
#             elif k == 1:
#                 man.work()
#             elif k == 2:
#                 man.eat()
#             else:
#                 man.play()
#                 print('поиграл')
#             d += 1
#             if man.home.no_food is True or man.nohungry < 0 or d > 365:
#                 break
#             print(f'еда = {man.home.food}',d)
#         return d
#
#
# class Home:
#     def __init__(self):
#         self.food = 50
#         self.money = 0
#         self.no_food = False
#
#
# def doit():
#     return random.randint(1, 6)
#
#
# man = Man()
# days = man.live()
#
# print(f'{man.name} прожил {days} дней и не умер, еды осталось {man.home.food}, денег осталось {man.home.money}')


# Задача 8. Блек-джек


# Задача 9. Крестики-нолики

# class Cell:
#     def __init__(self,n,m):
#         self.number = int(str(m) + str(n))
#         self.setn = '| |'
#         self.k = str(self.number) + str(self.setn)


# class Board:
#     def __init__(self):
#         self.field = [[Cell(i,j) for i in range(1,4)] for j in range(1,4)]
#
#     def pr_info(self):
#         for i in self.field:
#             for j in i:
#                 print(j.setn,end=' ')
#             print('\n')
#
#     def printing(self,znak,nomer):
#         for i in self.field:
#             for j in i:
#                 if j.number == nomer:
#                     j.setn = '|' + str(znak) + '|'
#             print('\n')
#
#     def check_win(self):
#         for i in self.field:
#             if (i[0].setn == i[1].setn and i[1].setn == i[2].setn) and i[0].setn != '| |':
#                 print(f'победил {i[0].setn}')
#                 return True
#         for i in range(3):
#             if (self.field[0][i].setn == self.field[1][i].setn == self.field[2][i].setn) and self.field[2][i].setn != '| |':
#                 print(f'победил {self.field[1][i].setn}')
#                 return True
#         if (self.field[0][0].setn == self.field[1][1].setn == self.field[2][2].setn) and self.field[2][2].setn != '| |':
#             print(f'победил {self.field[1][1].setn}')
#             return True
#         elif (self.field[2][0].setn == self.field[1][1].setn == self.field[0][2].setn) and self.field[0][2].setn != '| |':
#             print(f'победил {self.field[1][1].setn}')
#             return True
#         return False
#
#
# class Player:
#     def __init__(self,name,znak):
#         self.name = name
#         self.znak = znak
#
# def turn(b,p):
#     number = int(input('введите номер клетки: '))
#     b.printing(p.znak, number)
#     b.pr_info()
#     if b.check_win() is True:
#         print('end')
#         return True
#     return False
#
# p1 = Player('Tom','X')
# p2 = Player('Mike','O')
# b = Board()
#
# while True:
#     if turn(b,p1) is True:
#         break
#     if turn(b,p2) is True:
#         break


# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.set_age(age)
#         self.__count += 1
#
#     def __str__(self):
#         return f"{self.__name}, {self.__age}"
#
#     def get_count(self):
#         return self.__count
#
#     def set_age(self,age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
# p = Person('mi',12)
# print(p)
# print(p.get_count())


# class Ship:
#     def __init__(self,model):
#         self.__model = model
#
#     def __str__(self):
#         return '\n{model}'.format(
#             model=self.__model
#         )
#
#     def sail(self):
#         return f'{self.__model} плывет'
#
#
# class WarShip(Ship):
#     def __init__(self,model,gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def attack(self):
#         print(f'\n {self.sail()},атакуем оружием {self.gun}')
#
# warsip = WarShip('admiral', 'rainmetal')
# warsip.attack()
#
# class CargoShip(Ship):
#     def __init__(self,model):
#         super().__init__(model)
#         self.tonnage = 0
#
#     def load(self):
#         self.tonnage += 1
#
#     def unload(self):
#         self.tonnage -= 1
#
# car = CargoShip('mirniy')
# car.sail()

# class DivisionError(Exception):
#     pass
#
# a,d = 2,3
# if a/d < 1:
#     raise DivisionError

# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.set_age(age)
#         self.__count += 1
#
#     def __str__(self):
#         return f"{self.__name}, {self.__age}"
#
#     def get_count(self):
#         return self.__count
#
#     def set_age(self,age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#
# class Student(Person):
#     def __init__(self,name,age,unik):
#         super().__init__(name,age)
#         self.unik = unik
#
#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 info,
#                 f'{self.get_name()} учится в {self.unik}, ему {self.get_age()}'
#             )
#         )
#         return info
#
#
# s = Student('Mike',12,'BMSTU')
# print(s)


# class FlyAble:
#     def __init__(self,height,speed):
#         self.set_height(height)
#         self.set_speed(speed)
#
#     def __str__(self):
#         return f'высота {self.__height}, скорость {self.__speed}'
#
#     def set_height(self,height):
#         self.__height = height
#
#     def set_speed(self,speed):
#         self.__speed = speed
#
#     def get_speed(self):
#         return self.__speed
#
#     def get_height(self):
#         return self.__height
#
#     def settle_down(self):
#         self.set_height(0)
#
#
# class Batterfly(FlyAble):
#     def __init__(self,speed,height):
#         super().__init__(height,speed)
#         self.name = 'babochka'
#
#     def fly_up(self):
#         self.set_height(1)
#
#     def fly(self):
#         self.set_speed(1)
#
#
# class Rocket(FlyAble):
#     def __init__(self,name,speed,height):
#         super().__init__(height,speed)
#         self.name = name
#         self.__blowed = False
#
#     def __str__(self):
#         if self.get_blow() is True:
#             return 'ракета взорвалась'
#         else:
#             return f'высота ракеты {self.name} = {self.get_height()}, скорость = {self.get_speed()}'
#
#     def fly_up(self):
#         self.set_height(500)
#
#     def fly_ahead(self):
#         self.set_speed(1000)
#
#     def blow_up(self):
#         self.set_blow()
#
#     def set_blow(self):
#         self.__blowed = True
#
#     def get_blow(self):
#         return self.__blowed
#
# r = Rocket('союз',0,0)
# print(r)
# r.fly_up()
# print(r)
# r.fly_ahead()
# print(r)
# r.blow_up()
# print(r)

# docstring

class Unit:

    """
    Базовый класс юнита

    Args:
        hp (int): передается здоровье юнита
    """
    def __init__(self,hp):
        self.set_hp(hp)

    def __str__(self):
        return f'{self.get_hp()}'

    def get_hit(self,damage):
        self.__hp -= damage

    def set_hp(self,hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    """
    Геттер для получения здоровья
    :param hp: здоровье
    """

class Soldier(Unit):
    def get_hit(self,damage):
        self.set_hp(self.get_hp() - damage)

class Cityzen(Unit):
    def get_hit(self,damage):
        self.set_hp(self.get_hp() - 2*damage)

# u = Soldier(30)
# print(u)
# u.get_hit(20)
# print(u)
# cit = Cityzen(40)
# print(cit)
# cit.get_hit(20)
# print(cit)

# print(Unit.__doc__)


# Задача 1. Налоги

# class Property:
#     def __init__(self,worth):
#         self.set_worth(worth)
#         self.set_tax()
#
#     def set_worth(self,worth):
#         self.__worth = worth
#
#     def get_worth(self):
#         return self.__worth
#
#
# class Apartment(Property):
#     def set_tax(self):
#         self.__tax = self.get_worth() / 1000
#
#     def get_tax(self):
#         return self.__tax
#
#
# class Car(Property):
#     def set_tax(self):
#         self.__tax = self.get_worth() / 200
#
#     def get_tax(self):
#         return self.__tax
#
#
# class CountryHouse(Property):
#     def set_tax(self):
#         self.__tax = self.get_worth() / 500
#
#     def get_tax(self):
#         return self.__tax
#
#
# def summ(lis, s, mon):
#     for i in lis:
#         s += i.get_tax()
#     if mon < s:
#         return f'нехватает денег на налоги, налоги = {s}'
#     else:
#         return 'налоги оплачены'

# money = 1000
# car_price = 38000
# house_price = 150000
# countryhouse_price = 250000
# property_list = [Car(car_price),Apartment(house_price),CountryHouse(countryhouse_price)]
# print(summ(property_list,0, money))


# Задача 2. Карма

# class KillError(Exception):
#     name = 'KillError'
#     pass
#
#
# class DrunkError(Exception):
#     name = 'DrunkError'
#     pass
#
# class CarCrashError(Exception):
#     name = 'CarCrashError'
#     pass
#
#
# class GluttonyError(Exception):
#     name = 'GluttonyError'
#     pass
#
#
# class DepressionError(Exception):
#     name = 'DepressionError'
#     pass
#
# def one_day(karma,f,ex_list = [DepressionError,GluttonyError,CarCrashError,DrunkError,KillError]):
#     try:
#         karma += random.randint(1, 7)
#         if random.randint(1, 10) == 10:
#             ex = random.choice(ex_list)
#             f.write(str(ex.name+'\n'))
#             raise ex
#     except DepressionError:
#         karma -= 10
#     except GluttonyError:
#         karma -= 20
#     except CarCrashError:
#         karma -= 30
#     except DrunkError:
#         karma += 20
#     except KillError:
#         karma -= 50
#     return karma
#
# def karma_life(day = 0, karma = 0):
#     f = open('karma_log.txt','w')
#     while karma < 500:
#         day += 1
#         karma = one_day(karma,f)
#     return f'прожито дней ради кармы в 500: {day}'
#
# print(karma_life())


# Задача 3. Свой словарь

# class MyDict(dict):
#     def get(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             return 0
#
#
# p = MyDict({1: 'deff',2:'ewe',3:'wwww'})
# print(p.get(4))


# Задача 4. Компания

# class Person:
#     def __init__(self,name,surname,age):
#         self.set_name(name)
#         self.set_surname(surname)
#         self.set_age(age)
#
#     def set_name(self,name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_surname(self,surname):
#         self.__surname = surname
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#
# class Employee(Person):
#     def salary(self):
#         pass
#
# class Manager(Employee):
#     def __init__(self,name,surname,age,salary=13000):
#         super().__init__(name,surname,age)
#         self.set_salary(salary)
#
#     def set_salary(self,salary):
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#
# class Agent(Employee):
#     def __init__(self,name,surname,age,amount,salary=5000):
#         super().__init__(name,surname,age)
#         self.set_salary(amount, salary)
#
#     def set_salary(self,amount,salary):
#         self.__salary = amount*0.05 + salary
#
#     def get_salary(self):
#         return self.__salary
#
# class Worker(Employee):
#     def __init__(self,name,surname,age,hours):
#         super().__init__(name,surname,age)
#         self.__hours = hours
#         self.set_salary(hours)
#
#     def set_salary(self,hours):
#         self.__salary = hours*100
#
#     def get_salary(self):
#         return self.__salary
#
# list_employees = []
# for i in [Manager('mike','vazovski',24),Agent('ash','bradley',25,200000),Worker('babayka','mini',4,176)]:
#     for j in range(3):
#         list_employees.append(i)
# for i in list_employees:
#     print(i.get_name(),i.get_surname(),i.get_salary())


# Задача 5. А-а-автомобиль!

# class Car:
#     def __init__(self,base,angle):
#         self.set_base(base)
#         self.set_angle(angle)
#
#     def set_base(self,base):
#         self.__base = base
#
#     def get_base(self):
#         return self.__base
#
#     def set_angle(self,angle):
#         self.__angle = angle
#
#     def get_angle(self):
#         return self.__angle
#
#     def moove(self,rang):
#         new_base = [self.get_base()[0] + rang*math.cos(self.get_angle()),self.get_base()[1] + rang*math.sin(self.get_angle())]
#         return new_base
#
#     def change_angle(self,a):
#         self.set_angle(self.get_angle() + a)
#
#
# class Buss(Car):
#     def __init__(self,base,angle,passengers,money=0):
#         super().__init__(base,angle)
#         self.set_passengers(passengers)
#         self.set_money(money)
#
#     def __str__(self):
#         return f'В автобусе едут {self.get_passengers()} пассажиров, заработано {self.get_money()} денег. Текущая координата: {self.get_base()}, угол = {self.get_angle()}'
#
#     def set_passengers(self,passengers):
#         self.__passengers = passengers
#
#     def get_passengers(self):
#         return self.__passengers
#
#     def set_money(self,money):
#         self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def moove(self,rang):
#         new_base = [self.get_base()[0] + rang*math.cos(self.get_angle()),self.get_base()[1] + rang*math.sin(self.get_angle())]
#         self.set_base(new_base)
#         self.set_money(self.get_money() + 10*self.get_passengers())
#         return new_base
#
#     def enter(self,n):
#         self.set_passengers(self.get_passengers() + n)
#
#     def out(self,n):
#         if n <= self.get_passengers():
#             self.set_passengers(self.get_passengers() - n)
#         else:
#             self.set_passengers(0)
#
#
# b = Buss([1,1],30,4)
# while b.get_passengers() < 25:
#     b.moove(20)
#     b.enter(3)
#     print(b)
#     b.out(1)
#     b.change_angle(8)
# while b.get_passengers() > 0:
#     b.moove(35)
#     b.enter(1)
#     print(b)
#     b.out(4)
#     b.change_angle(10)


# Задача 6. Совместное проживание 2

# class Home:
#     def __init__(self,money=100,food=50,catfood=30,dirt=0):
#         self.set_money(money)
#         self.set_food(food)
#         self.set_catfood(catfood)
#         self.set_dirt(dirt)
#
#     def __str__(self):
#         return f'В доме {self.get_money()} денег, {self.get_food()} еды в холодильнике, {self.get_catfood()} еды котика, грязи - {self.get_dirt()}'
#
#     def set_money(self,money):
#         self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def set_food(self,food):
#         self.__food = food
#
#     def get_food(self):
#         return self.__food
#
#     def set_catfood(self,catfood):
#         self.__catfood = catfood
#
#     def get_catfood(self):
#         return self.__catfood
#
#     def set_dirt(self,dirt):
#         self.__dirt = dirt
#
#     def get_dirt(self):
#         return self.__dirt
#
#     def new_day(self,husband,wife,cat):
#         self.set_dirt(self.get_dirt() + 5)
#         if self.get_dirt() >= 90:
#             husband.set_ishappy(husband.get_ishappy() - 10)
#             wife.set_ishappy(wife.get_ishappy() - 10)
#         husbanddo = random.randint(1,2)
#         wifedo = random.randint(1,3)
#         catdo = random.randint(1,2)
#         if husbanddo == 1:
#             husband.play()
#         elif husbanddo == 2:
#             husband.work(self)
#         husband.human_eat(self, random.randint(10, 15))
#         if wifedo == 1:
#             wife.buy_catfood(self,30)
#         elif wifedo == 2:
#             wife.buy_food(self,90)
#         elif wifedo == 3:
#             wife.home_clean(self)
#         wife.human_eat(self,random.randint(10,12))
#         cat.cat_eat(self,9)
#         if catdo == 1:
#             cat.sleep()
#         elif catdo == 2:
#             cat.drat_oboi(self)
#         if random.randint(1,91) == 45:
#             wife.buy_shuba(self)
#
#
# class HomeUnit:
#     def __init__(self,name,ishunger=30):
#         self.set_name(name)
#         self.set_ishunger(ishunger)
#         self.set_dead(False)
#
#     def set_dead(self, flag):
#         self.__dead = flag
#
#     def get_dead(self):
#         return self.__dead
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_ishunger(self, ishunger):
#         self.__ishunger = ishunger
#
#     def get_ishunger(self):
#         return self.__ishunger
#
#     def human_eat(self,home,foodamount):
#         self.set_ishunger(self.get_ishunger() + foodamount)
#         home.set_food(home.get_food() - foodamount)
#
#     def cat_eat(self,home,foodamount):
#         self.set_ishunger(self.get_ishunger() + foodamount)
#         home.set_catfood(home.get_catfood() - foodamount)
#
#
# class Husband(HomeUnit):
#     def __init__(self,name,ishunger=30,ishappy=100):
#         super().__init__(name,ishunger)
#         self.set_ishappy(ishappy)
#
#     def __str__(self):
#         return f'{self.get_name()}, уроваень счастья: {self.get_ishappy()}, уровень сытости: {self.get_ishunger()}'
#
    # def set_ishappy(self, ishappy):
    #     self.__ishappy = ishappy
    #     if self.__ishappy < 0:
    #         self.set_dead(True)
#
#     def get_ishappy(self):
#         return self.__ishappy
#
#     def play(self):
#         self.set_ishunger(self.get_ishunger() - 10)
#         self.set_ishappy(self.get_ishappy() + 20)
#
#     def work(self,home):
#         self.set_ishunger(self.get_ishunger() - 10)
#         home.set_money(home.get_money() + 150)
#
#     def glady_kota(self,cat):
#         self.set_ishunger(self.get_ishunger() - 10)
#         self.set_ishappy(self.get_ishappy() + 5)
#
# class Wife(HomeUnit):
#     def __init__(self,name,ishunger=30,ishappy=100):
#         super().__init__(name,ishunger)
#         self.set_ishappy(ishappy)
#
#     def __str__(self):
#         return f'{self.get_name()}, уроваень счастья: {self.get_ishappy()}, уровень сытости: {self.get_ishunger()}'
#
    # def set_ishappy(self, ishappy):
    #     self.__ishappy = ishappy
    #     if self.__ishappy < 0:
    #         self.set_dead(True)
#
#     def get_ishappy(self):
#         return self.__ishappy
#
#     def buy_food(self,home,newfood):
#         self.set_ishunger(self.get_ishunger() - 10)
#         home.set_food(home.get_food() + newfood)
#         home.set_money(home.get_money() - newfood)
#
#     def buy_catfood(self,home,newfood):
#         self.set_ishunger(self.get_ishunger() - 10)
#         home.set_catfood(home.get_catfood() + newfood)
#         home.set_money(home.get_money() - newfood)
#
#     def buy_shuba(self,home):
#         self.set_ishunger(self.get_ishunger() - 10)
#         self.set_ishappy(self.get_ishappy() + 60)
#         home.set_money(home.get_money() - 350)
#
#     def home_clean(self,home):
#         if home.get_dirt() > 60:
#             home.set_dirt(home.get_dirt() - 80)
#
# class Cat(HomeUnit):
#     def __init__(self, name, ishunger=10):
#         super().__init__(name, ishunger)
#
#     def __str__(self):
#         return f'{self.get_name()}, уровень сытости: {self.get_ishunger()}'
#
#     def drat_oboi(self,home):
#         home.set_dirt(home.get_dirt() + 5)
#
#     def sleep(self):
#         pass
#
# home = Home()
# h = Husband('Mike')
# w = Wife('Eleonora')
# c = Cat('Barsik')
#
# for i in range(366):
#     if h.get_dead() == True or w.get_dead() == True or c.get_dead() == True:
#         break
#     else:
#         home.new_day(h,w,c)
#         print(home)
#         print(h,w,c)


# Задача 7. Стек
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return ' '.join(self.stack)
#
#     def pop(self):
#         try:
#             removed = self.stack.pop()
#             return removed
#         except IndexError:
#             return None
#
#     def push(self,item):
#         self.stack.append(item)
#
# class Manager:
#     def __init__(self):
#         self.stack = dict()
#
#     def __str__(self):
#         display = []
#         if self.stack:
#             for i in sorted(self.stack.keys()):
#                 print(self.stack[i])
#                 display.append(f'{str(i)} {self.stack[i]} \n')
#         return ''.join(display)
#
#
#     def add_task(self,item,n):
#         if n not in self.stack:
#             self.stack[n] = Stack()
#         self.stack[n].push(item)
#
# manager = Manager()
# manager.add_task("сделать уборку", 4)
# manager.add_task("помыть посуду", 4)
# manager.add_task("отдохнуть", 1)
# manager.add_task("поесть", 2)
# manager.add_task("сдать дз", 2)
# print(manager)
