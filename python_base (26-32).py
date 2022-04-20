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
import functools
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


# Декораторы

import time
# from itertools import count
from typing import Callable,Any
#
#
# def timer(func: Callable, *args, **kwargs) -> Any:
#     start_time = time.time()
#     result = func(*args, **kwargs)
#     end_time = time.time()
#     print(round(end_time-start_time,4))
#
#     return result
#
# def square_sum(n) -> int:
#     result = 0
#     for _ in range(n+1):
#         result += sum([i_num**2 for i_num in range(10000)])
#
#     return result
#
# print(timer(square_sum,10))


# def func_1(x):
#
#     return x + 10
#
# def func_2(function: Callable, *args, **kwargs) -> Any:
#     print(function(*args, **kwargs))
#     return function(*args, **kwargs)*function(*args, **kwargs)
#
# print(func_2(func_1,3))


# def decor(function):
#     def wrapped_function(*args,**kwargs):
#         for i in range(2):
#             function(*args, **kwargs)
#         return
#     return wrapped_function
#
#
# @decor
# def greeting(name):
#     print(f'Привет, {name}!')
#
#
# greeting('Tom')


# def decor(function):
#     def wrapped_function(*args, **kwargs):
#         start = time.time()
#         function(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return
#     return wrapped_function
#
# @decor
# def fib(n):
#     s=1
#     for i in range(1000):
#         s*=n
#     return s
#
# fib(2000000)


# def bread(function):
#     def wrapped_function(*args,**kwargs):
#         print('</----------\>')
#         function(*args,**kwargs)
#         print('</----------\>')
#         return
#     return wrapped_function
#
#
# def ingredients(function):
#     def wrapped_function(*args,**kwargs):
#         print('#помидоры#\n--ветчина-\n-~салат~')
#         function(*args,**kwargs)
#         return
#     return wrapped_function
#
#
# @bread
# @ingredients
# def sandwich():
#     print('шаурмаааааа')
#     return


# PLUGINS = dict()
#
# def regusret(function):
#     PLUGINS[function.__name__] = function
#     return function
#
# @regusret
# def bread(function):
#     def wrapped_function(*args,**kwargs):
#         print('</----------\>')
#         function(*args,**kwargs)
#         print('</----------\>')
#         return
#     return wrapped_function
#
# @regusret
# def ingredients(function):
#     def wrapped_function(*args,**kwargs):
#         print('#помидоры#\n--ветчина-\n-~салат~')
#         function(*args,**kwargs)
#         return
#     return wrapped_function
#
# @regusret
# def sandwich():
#     print('шаурмаааааа')
#     return
#
#
# print(PLUGINS)
# print(sandwich())


# 1 Broken decorator

# def bread(function):
#     def wrapped_function(*args,**kwargs):
#         input('как дела?\n')
#         print('а у менян ')
#         function(*args,**kwargs)
#         return
#     return wrapped_function
#
#
# @bread
# def sandwich():
#     print('что происходит')
#     return
#
# sandwich()


# Задача 2. Замедление кода

# def bread(function):
#     def wrapped_function(*args,**kwargs):
#         time.sleep(3)
#         function(*args,**kwargs)
#         return
#     return wrapped_function
#
#
# @bread
# def sandwich():
#     print('что происходит')
#     return
#
# sandwich()


# Задача 3. Логирование

# import functools
#
#
# def bread(function):
#     @functools.wraps(function)
#     def wrapped_function(*args,**kwargs):
#         function(*args,**kwargs)
#     return wrapped_function
#
#
# @bread
# def sandwich():
#     """документация"""
#     try:
#         print(5 / 0)
#         return
#     except ZeroDivisionError:
#         f = open('log.txt', 'w')
#         f.write(f'{ValueError.__name__}, {sandwich.__name__}')
#     return
#
# sandwich()

from functools import partial

# def debug_decor(function: Callable) -> Callable:
#     def wrapped_function(*args, **kwargs):
#         result = function(*args, **kwargs)
#         print(f'В функцию {function.__name__}, переданы аргументы: {list(f"{arg}" for arg in args)} и keywords {list(f"{k}={v}" for k,v in kwargs.items())}')
#         print(f'функция {function.__name__}, вернула значение {result}')
#         return result
#     return wrapped_function
#
#
# @debug_decor
# def greeting(name, age=None):
#     if age:
#         return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
#     else:
#         return "Привет, {name}!".format(name=name)
#
#
# greeting("Том")
# greeting("Миша", age=100)
# greeting(name="Катя", age=16)


# Задача 5. Счётчик

# PLUGINS = dict()
#
# def counter(function: Callable) -> Callable:
#     PLUGINS[function.__name__] = function
#     PLUGINS[function.__name__ + '_count'] = 0
#     def wrapped_function(*args,**kwargs) -> None:
#         function(*args,**kwargs)
#         PLUGINS[function.__name__ + '_count'] += 1
#         print(f'Функция {function.__name__} была вызвана {PLUGINS[function.__name__ + "_count"]} раза')
#         return
#     return wrapped_function
#
#
# @counter
# def sandwich():
#     # print('шаурмаааааа')
#     return
#
#
# @counter
# def bread():
#     return
#
# sandwich()
# sandwich()
# sandwich()
# sandwich()
# bread()
# bread()
# bread()
# print(PLUGINS)


# MRO - Множественное наследование


# class FlyAble:
#     def __init__(self,model):
#         self.height = 0
#         self.speed = 0
#         self.model = model
#
#     def move(self):
#         self.speed += 10
#
#     def fly_up(self):
#         self.height = 100
#
#     def set_down(self):
#         self.height = 0
#
#     def stop(self):
#         self.speed = 0
#
#
# class Robot:
#     def __init__(self,model):
#         self.model = model
#
#     def __str__(self):
#         return f'я робот {self.model}'
#
#
# class Searcher(FlyAble,Robot):
#     def __init__(self,model):
#         super().__init__(model)
#
#     def __str__(self):
#         return f'я робот сёрчер'
#
# class WarRobot(FlyAble,Robot):
#     def __init__(self,model,weapon):
#         super().__init__(model)
#         self.weapon = weapon
#
#
#
#     def __str__(self):
#         return f'защищаю объект оружием {self.weapon}, модель {self.model}'
#
#
# s = Searcher(model=1)
# print(s)
# print(s.model,s.speed,s.height)
#
# w = WarRobot(model=2,weapon='минаган')
# print(w)
# w.fly_up()
# print(w.height)


# Задача 1. Транспорт

from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     def __init__(self,color):
#         self.color = color
#         self.speed = 0
#
#     @abstractmethod
#     def move(self,speed):
#         self.speed = speed
#
#
# class Car(Transport):
#     def __init__(self,color):
#         super().__init__(color)
#         self.ground_move = True
#         self.water_move = False
#
#     def move(self,speed):
#         self.speed = speed
#
#
# class Play:
#     def play_music(self,music):
#         self.music = music
#
#
# class Boat(Transport):
#     def __init__(self,color):
#         super().__init__(color)
#         self.ground_move = False
#         self.water_move = True
#
#     def move(self,speed):
#         self.speed = speed
#
#
# class Amphib(Transport, Play):
#     def __init__(self,color):
#         super().__init__(color)
#         self.ground_move = False
#         self.water_move = True
#         self.music = 'nothing'
#
#     def move(self,speed):
#         self.speed = speed
#
# a = Amphib('red')
# a.play_music('california')
# print(a.music)


# class Figure(ABC):
#     def __init__(self,x,y,lenght,width):
#         self.x = x
#         self.y = y
#         self.lenght = lenght
#         self.width = width
#
#     @abstractmethod
#     def move(self,x,y):
#         self.x += x
#         self.y += y
#
#
# class Resize:
#     def resize(self,lenght,height):
#         self.lenght = lenght
#         self.height = height
#
#
# class Rectangle(Figure,Resize):
#     def __init__(self, x, y, lenght, height):
#         super().__init__(x, y, lenght, height)
#
#     def move(self, x, y):
#         self.x += x
#         self.y += y
#
#
# class Square(Figure, Resize):
#     def __init__(self, x, y, size):
#         super().__init__(x, y, size, size)
#
#     def move(self, x, y):
#         self.x += x
#         self.y += y
#
#
# s = Square(1, 2, 43)
# s.move(4, 3)
# print(s.y)

# s.resize(12,23)
# print(s.lenght)


# Контекстный менеджер

# class File:
#     def __init__(self,name,tip):
#         self.name = name
#         self.tip = tip
#
#     def __enter__(self):
#         print(f'открываем файл {self.name}')
#         self.file = open(self.name, self.tip)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#         pass
#
# with File('example.txt', 'w') as file:
#     file.file.write('Всем привет!')


# class Example:
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#         print(f'Вызов __init__ \nВызов __enter__')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if Exception:
#             print(f'Тип ошибки {Exception}\nЗначение ошибки: {Exception.__doc__}\nСлед ошибки: {Exception.__context__}\n Вызов __exit__')
#         return True
#
#
# my_obj = Example()
# with my_obj as obj:
#     print('Код внутри первого вызова контекст менеджера')
#     with my_obj as obj2:
#         raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
#
#     print('Я обязательно выведусь...')


# class Transport(ABC):
#     def __init__(self,color):
#         self.__color = color
#         self.__speed = 0
#
#     def __str__(self):
#         return f'{self.color}, {self.speed}'
#
#     def move(self,speed):
#         self.__speed = speed
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self,color):
#         self.__color = color
#
#     @property
#     def speed(self):
#         return self.__speed
#
#     @speed.setter
#     def speed(self, speed):
#         self.__speed = speed
#
# class Car(Transport):
#     def __init__(self,color):
#         super().__init__(color)
#         self.ground_move = True
#         self.water_move = False
#
#
# class Play:
#     def play_music(self,music):
#         self.__music = music
#
#     @property
#     def music(self):
#         return self.__music
#
#     @music.setter
#     def music(self, music):
#         self.__music = music
#
#
# class Boat(Transport):
#     def __init__(self,color):
#         super().__init__(color)
#         self.ground_move = False
#         self.water_move = True
#
#     def move(self,speed):
#         self.__speed = speed
#
#
# class Amphib(Transport, Play):
#     def __init__(self,color):
#         super().__init__(color)
#         self.ground_move = False
#         self.water_move = True
#         self.__music = 'nothing'
#
#
# a = Amphib('red')
# print(a)
# a.play_music('california')
# print(a.music)


# class File:
#     def __init__(self, name, optype):
#         self.__name = name
#         self.__optype = optype
#
#     @property
#     def optype(self):
#         return self.__optype
#
#     @optype.setter
#     def optype(self,optype):
#         self.__optype = optype
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     def __enter__(self):
#         if os.path.isfile(self.name):
#             print(f'открываем файл {self.name}')
#             self.file = open(self.name, self.optype)
#         else:
#             self.file = open(self.name, 'w')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return
#
#
# my_obj = File('exampl.txt','r')
# with my_obj as obj:
#     print('ok')



# Задача 2. Математический модуль

# class MyMath:
#     def __init__(self):
#         pass
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self,side):
#         self.__side = side
#
#     @property
#     def r(self):
#         return self.__r
#
#     @r.setter
#     def r(self, r):
#         self.__r = r
#
#     @classmethod
#     def circle_len(cls,r):
#         return 2*math.pi*r
#
#     @classmethod
#     def circle_sq(cls,r):
#         return math.pi*r**2
#
#     @classmethod
#     def qube_volume(cls,side):
#         return side**3
#
#     @classmethod
#     def square_surface(cls,r):
#         return 4/3*math.pi*r**3
#
#
# res_1 = MyMath.circle_len(r=5)
# res_2 = MyMath.circle_sq(r=6)
# res_3 = MyMath.square_surface(6)
# print(res_1)
# print(res_2)
# print(res_3)


# Задача 3. Моделирование

# class Triangle:
#     def __init__(self,base,height):
#         self.__base = base
#         self.__height = height
#
#     def square_triangle(self):
#         return self.base*self.height/2
#
#     def perimetr_triangle(self):
#         return self.base + math.sqrt((self.base/2)**2 + self.height**2)*2
#
#     @property
#     def base(self):
#         return self.__base
#
#     @base.setter
#     def base(self,base):
#         self.__base = base
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#
# class Kvadrat:
#     def __init__(self, side1, side2):
#         self.__side1 = side1
#         self.__side2 = side2
#
#     def square_kvadrat(self):
#         return self.side1 * self.side2
#
#     def perimetr_kvadrat(self):
#         return self.side1 + self.side2
#
#     @property
#     def side1(self):
#         return self.__side1
#
#     @side1.setter
#     def side1(self, side1):
#         self.__side1 = side1
#
#     @property
#     def side2(self):
#         return self.__side2
#
#     @side2.setter
#     def side2(self, side2):
#         self.__side2 = side2
#
#
# class SquareFigureMixin:
#     def square_figure(self):
#         return sum(self.square_list)
#
#
# class Pyramid(Triangle,SquareFigureMixin):
#     def __init__(self,base,height):
#         super().__init__(base,height)
#         self.square_list_set(base,height)
#
#     @property
#     def square_list(self):
#         return self.__square_list
#
#     def square_list_set(self,base,height):
#         self.__square_list = [base*base] + [base*height for _ in range(4)]
#
#
# class Qube(Kvadrat,SquareFigureMixin):
#     def __init__(self, side1, side2,side3):
#         super().__init__(side1, side2)
#         self.side3 = side3
#         self.square_list_set(side1, side2, side3)
#
#     @property
#     def side3(self):
#         return self.__side3
#
#     @side3.setter
#     def side3(self, side3):
#         self.__side3 = side3
#
#     @property
#     def square_list(self):
#         return self.__square_list
#
#     def square_list_set(self, side1, side2,side3):
#         self.__square_list = [self.square_kvadrat()]*2 + [side1 * side3]*2 + [side2 * side3]*2
#
# p = Pyramid(3,4)
# print(p.square_list)
# print(p.square_figure())
# p = Qube(3,4,5)
# print(p.square_list)
# print(p.square_figure())



# Задача 4. Дата


# class Date:
#     def __init__(self,day,month,year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self):
#         return f'День: {self.day}    Месяц: {self.month}    Год: {self.year}'
#
#     @classmethod
#     def is_date_valid(cls,string: str) -> bool:
#         lst = string.split('-')
#         return (int(lst[0]) in range(1, 32)) and (int(lst[1]) in range(1, 13)) and int(lst[2]) >= 1
#
#     @classmethod
#     def from_string(cls,string: str) -> "Date":
#         day,month,year = map(int,string.split('-'))
#         date = cls(day,month,year)
#         return date
#
# date = Date.from_string('10-12-2077')
# print(date)
# print(Date.is_date_valid('10-11-2077'))
# print(Date.is_date_valid('40-12-2077'))



# Продвинутые декораторы #


# 29.2 Декоратор context manager

from contextlib import contextmanager
from collections.abc import Iterator

# @contextmanager
# def next_num(num: int) -> Iterator:
#     print('старт')
#     try:
#         yield num + 1
#     except ZeroDivisionError as zde:
#         print(zde)
#     finally:
#         print('код все равно сработал')
#     print('финиш')
#
# with next_num(-1) as next:
#     for i in range(4):
#         print(f'next = {next}')
#         print(10/next)


# @contextmanager
# def timer() -> Iterator:
#     start = time.time()
#     try:
#         yield
#     finally:
#         print(time.time() - start)
#
# with timer() as t:
#     v = 100 ** 1000000


# @contextmanager
# def in_dir(dir):
#     try:
#         print(f'тут все папки из вашего диска {dir}:', end=' ')
#         dir = 'C:\X\GitHub\Basic_courses'
#         yield dir
#     finally:
#         pass
#
# with in_dir('C:\\'):
#     print(os.listdir())


import functools
from datetime import datetime


# def createtime(cls):
#     @functools.wraps(cls)
#     def wrapper(*args,**kwargs):
#         instance = cls(*args,**kwargs)
#         print(f'время создания экземпляра: {datetime.utcnow()}')
#         print(', '.join(dir(cls)))
#         return instance
#     return wrapper
#
#
# @createtime
# class Func:
#     def __init__(self,n):
#         self.n = n
#
#     def m1(self):
#         pass
#
#     def m2(self):
#         pass
#
# f1 = Func(1000)
# f2 = Func(73843874**3474)
# f3 = Func(43**2933293)


# def logger(function):
#     @functools.wraps(function)
#     def wrapped_function(*args, **kwargs):
#         print(function, function.__doc__, *args, **kwargs)
#         result = function(*args, **kwargs)
#         return result
#     return wrapped_function
#
# def for_all_methods(logger):
#     @functools.wraps(logger)
#     def decorate(cls):
#         for i in dir(cls):
#             if i.startswith('__') is False:
#                 current = getattr(cls, i)
#                 decorated = logger(current)
#                 setattr(cls, i, decorated)
#         return cls
#     return decorate
#
# @for_all_methods(logger)
# class Bomb:
#     def __init__(self):
#         self.mass = 500
#
#     def explode(self):
#         self.mass = 0
#
# tsar = Bomb()
# tsar.explode()
# print(tsar.mass)


# Задача 1. Права доступа

# user_permissions = ['admin']
#
#
# def check_permission(user_name):
#     def decorator(function):
#         def wrap(*args,**kwargs):
#             try:
#                 if user_name in user_permissions:
#                     result = function(*args,**kwargs)
#                     return result
#                 else:
#                     raise PermissionError
#             except PermissionError: print(f'{PermissionError.__name__} - '
#                                           f'У пользователя недостаточно прав, чтобы выполнить функцию {function.__name__}')
#             return
#         return wrap
#     return decorator
#
#
# @check_permission('admin')
# def delete_site():
#     print('Удаляем сайт')
#
#
# @check_permission('user_1')
# def add_commentede():
#     print('Добавляем комментарий')
#
#
# delete_site()
# add_commentede()


# Задача 2. Функция обратного вызова

# @callback('//')
# def example():
#     print('Пример функции, которая возвращает ответ сервера')
#     return 'OK'
#
#
# route = '//'
# if route:
#     response = example()
#     print('Ответ:', response)
# else:
#     print('Такого пути нет')


# Задача 3. Логирование в формате

