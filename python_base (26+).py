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

def prost(n):
    if n==0 or n==1:
        return True
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def prost_gen(n):
    count = 0
    number = 1
    r = 1
    while count <= n:
        yield r
        while prost(number) is False:
            number += 1
        r = number
        number += 1
        count += 1


for i in prost_gen(5):
    print(i)

