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


