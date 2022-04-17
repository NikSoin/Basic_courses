# Итераторы

# def iterate(s):
#     i = 0
#     while True:
#         try:
#             print(s[i])
#         except IndexError:
#             print('конец итерации')
#             break
#         i += 1
#
# s = [1,2,3,4,5]
# iterate(s)


# import  random
#
# class RandomNumber:
#     def __init__(self,limit):
#         self.__limit = limit
#         self.__counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__counter < self.__limit:
#             self.__counter += 1
#             return random.randint(0,10)
#         else:
#             raise StopIteration
#
# it = RandomNumber(limit=4)
# for i in it:
#     print(i)


# class Fibonacci:
#     """Итератор фибоначчи"""
#
#     def __init__(self,n):
#         self.counter = 0
#         self.current = 0
#         self.next = 1
#         self.n = n
#
#     def __iter__(self):
#         self.counter = 0
#         self.current = 0
#         self.next = 1
#         return self
#
#     def __next__(self):
#         self.counter += 1
#         if self.counter > 1:
#             if self.counter > self.n:
#                 raise StopIteration
#             self.current, self.next = self.next, self.current + self.next
#         return self.current
#
#
# fib_iterator = Fibonacci(1000000)
# print(6 in fib_iterator)


# class СountIterator:
#     def __init__(self):
#         self.count = 0
#
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         r = self.count
#         self.count += 1
#         return r
#
#
# my_iter = СountIterator()
# for i_elem in my_iter:
#     print(i_elem)
# import random
#
#
# class Endless:
#     def __init__(self,c):
#         self.current = random.random()
#         self.next = self.current + random.random()
#         self.count = 0
#         self.c = c
#
#     def __iter__(self):
#         self.count = 0
#         self.current = random.random()
#         self.next = self.current + random.random()
#         return self
#
#     def __next__(self):
#         if self.count == self.c:
#             raise  StopIteration
#         self.count += 1
#         self.current,self.next = self.next, self.next + random.random()
#         return self.current
#
# for i in Endless(2):
#     print(i)
#
# for i in Endless(3):
#     print(i)


# Задача 3. Простые числа

# class Primes:
#     def __init__(self,n):
#         self.start = 1
#         self.count = 0
#         self.n = n
#
#     def __iter__(self):
#         self.start = 1
#         self.count = 0
#         return  self
#
#     def __next__(self):
#         self.count += 1
#         if self.count <= self.n:
#             while prost(self.start) is False:
#                 self.start += 1
#             r = self.start
#             self.start += 1
#             return r
#         else:
#             raise StopIteration
#
#
# def prost(n):
#     if n==0 or n==1:
#         return True
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem,end=' ')


# Генераторы

# def fibon(n):
#     current = 0
#     next = 1
#     for _ in range(n):
#         yield current
#         current, next = next, current + next
#
# fib = fibon(n=10)
# for i in fib:
#     print(i)


# Задача 1. Бесконечный генератор

# def endless():
#     number = 0
#     while True:
#         yield number
#         number += 1
#
# for i in endless():
#     print(i)

# def prost(n):
#     if n==1:
#         return True
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
# def prost_gen(n):
#     count = 0
#     number = 1
#     r = 1
#     while count <= n:
#         yield r
#         while prost(number) is False:
#             number += 1
#         r = number
#         number += 1
#         count += 1
#
#
# for i in prost_gen(5):
#     print(i)



# def read(f):
#     c = int(f[0])
#     for i in range(len(f)):
#         c = int(f[i])
#         yield c
#
#
# s = 0
# f = '4 2 3 5'
# for i in read(f.split()):
#     s += i
# print(s)


# Аннотация типов данных
# def greeting(name: str) -> str:
#     return 'Hello ' + str(name)
#
# print(greeting(12))


# class Squared:
#     def __init__(self,number):
#         self.set_number(number)
#
#     def set_number(self,number):
#         self.__number = number
#
#     def __iter__(self):
#         self.start = 0
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start < self.__number:
#             return f'{self.start}**{2} = {self.start**2}'
#         else:
#             raise StopIteration
#
# for j in Squared(10):
#     print(j)


import math

# def squared(n: int,r = 1) -> int:
#     while r <= n:
#         yield r**2
#         r += 1
#
# for i in squared(10):
#     print(f'{i}')


# for j in [i**2 for i in range(1,11)]:
#     print(j)


# Задача 2. Рефакторинг

# def rebound(list_1: list,list_2: list) -> None:
#     for x in list_1:
#         for y in list_2:
#             result = x * y
#             yield x,y,result
#
# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
# for i in rebound(list_1,list_2):
#     if i[2] == to_find:
#         print(f'число {to_find} можно получить перемножением чисел {i[0]} и {i[1]}')
#         break


# Задача 3. Пути файлов
import os


# def gen_files_path(path,find):
#     for (dirpath, dirnames, filenames) in os.walk(path):
#         yield filenames
#         if find in dirnames:
#             print(f'найден {find}')
#             break
#         else:
#             for j in dirnames:
#                 gen_files_path(os.path.join(path, j),find)
#
#
# a = []
# for i in gen_files_path('C:\X\GitHub','__pycache__'):
#     a.extend(i)
# for i in a:
#     print(i)


# Задача 4. Последовательность Хофштадтера

# class Hoff:
#     def __init__(self,stop):
#         self.__stop = stop
#         self.start = 1
#
#     def __iter__(self):
#         self.start = 1
#         self.number_start = 1
#         return self
#
#     def __next__(self):
#         if self.start <= self.__stop:
#             next = Q(self.start)
#             self.start += 1
#             return next
#         else:
#             raise StopIteration
#
#
# def  Q(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return Q(n - Q(n-1)) + Q(n - Q(n-2))
#
#
# for i in Hoff(25):
#     print(i,end=' ')


# Задача 5. Количество строк

# def str_counter(path):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file[-3:] == 'txt':
#                 f = open(os.path.join(root,file),'r')
#                 for i in f:
#                     if i[0] != '#' and i != '\n':
#                         yield 1
#
# s = 0
# for i in str_counter("C:\X\GitHub"):
#     s += i
# print(s)


# Задача 6. Односвязный список

# class LinkedList:
#     def __init__(self):
#         self.set_list([])
#
#     def __str__(self):
#         return str(self.get_list())
#
#     def set_list(self,list):
#         self.__list = list
#
#     def get_list(self):
#         return self.__list
#
#     def app_end(self,n):
#         self.set_list(self.get_list() + [n])
#
#     def get(self,index):
#         return self.get_list()[index]
#
#     def remove(self,index):
#         new_list = []
#         for i,j in enumerate(self.get_list()):
#             if i != index:
#                 new_list += [j]
#         self.set_list(new_list)
#
#
#
# from typing import Any, Optional
#
#
# class Node:
#     def __init__(self,value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
#         self.value = value
#         self.next = next
#
#     def __str__(self):
#         return f'Node [{str(self.value)}]'
#
# class LinkedList:
#     def __init__(self) -> None:
#         self.head: Optional[Node] = None
#         self.len = 0
#
#     def __str__(self):
#         current = self.head
#         values = [str(current.value)]
#         while current.next is not None:
#             current = current.next
#             values.append(str(current.value))
#         return f'{values}'
#
#     def app_end(self,n: Any) -> None:
#         new_node = Node(n)
#         if self.head is None:
#             self.head = new_node
#             return
#
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#         self.len += 1
#
#     def remove(self,index):
#         cur = self.head
#         cur_index = 0
#         if self.len==0 or index > self.len:
#             raise IndexError
#         if cur is not None:
#             if index == 0:
#                 self.head = cur.next
#                 self.len -= 1
#                 return
#         while cur is not None:
#             if cur_index == index:
#                 break
#             prev = cur
#             cur = cur.next
#             cur_index += 1
#
#         prev.next = cur.next
#         self.len -= 1
#         return
#
#     def get(self,index):
#         cur_index = 0
#         if index == 0:
#             return self.head
#         current = self.head
#         while current.next:
#             cur_index += 1
#             if cur_index == index:
#                 return current.value
#             current = current.next
#
#
# my_list = LinkedList()
# my_list.app_end(10)
# my_list.app_end(20)
# my_list.app_end(30)
# print('Текущий список:', my_list)
# print('Получение третьего элемента:', my_list.get(2))
# print('Удаление второго элемента.')
# my_list.remove(1)
# print('Новый список:', my_list)


