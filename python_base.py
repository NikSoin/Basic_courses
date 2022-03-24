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
# import random
# b = 100
# m = 0
# c = int(input('zagadai chislo: '))
# n = random.randint(m,b)
# while(True):
#     print(m,b)
#     ot = int(input(f'Твое число =(1), >(2), <(3) {n}?'))
#     if(ot == 1):
#         break
#     elif(ot == 2):
#         m = n
#         n = random.randint(m,b)
#     elif(ot == 3):
#         b = n
#         n = random.randint(m,b)
# print('ugadal')
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


