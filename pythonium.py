-------/////PYTHONIUM/////--------

Данный документ призван описать все базовые концепции языка Python и собрать их воедино в общей системе.
Львиная доля данной информации взята с лекции Udemy: Полное руководство по Python 3: от новичка до специалиста.

Документ будет разбит на разделы, которые в свою очередь разбиты на главы. Нумерация может отличатся от
той, что на Udemy, но названия глав и разделов идентичны.

Автор документа: Ryzhov Alexander.
06.09.2020 created

=
-----РАЗДЕЛ 1: Введение в Python-----
=

1. Скачать исходный код

	ссылка - https://1drv.ms/u/s!AqtQeAOHZEjQuKNOslckCDk4zl4htA?e=afD6J2

2. Присоединиться к чату в Telegram

	ссылка - https://t.me/python_devs

3. Почему Python?

	-Синтаксис
	-Open Source
	-Лёгкий
	-Популярен для бизнеса
	-Автоматизация
	-Десктоп, Андроид, Веб, Машинное обучение

4. Python с технической точки зрения

	-ЯП общего назначения
	-Строгая типизация
	-Динамический
	-Интерпретируемый(предварительно компилируется в байт-код)
	-Мультипарадигмальный
	-CPython - основная реализация Python

5. Python 2 vs Python 3

	-В данном документе будет рассматриваться только Python 3.

6. Стандартная библиотека
	
	Официальная документация - docs.python.org

7. Редакторы кода

	-Автором используется Sublime text или встроенный в Udemy редактор, предназначенный для проверки задач.

8. Инсталлируем дистрибутив Anaconda

	-Anaconda автором данного документа не рассматривается

9. Введение в Anaconda

	-Anaconda автором данного документа не рассматривается

10. Jupyter Notebook не запускается через Anaconda Navigator?

	-Anaconda автором данного документа не рассматривается

=
-----Раздел 2: Основы Python-----
=

11. Обзор основных типов данных

Python работает в кодировке Unicode - каждый символ представляет 2 байта.
	Типы данных:
		Целые числа-int
			1,2,3
		Числа с плавающей точкой-float
			1.1, 2.4, 3.0
		Строки-str - последовательность символов
			"Hello"
		Списки-list - последовательность объектов
			[1, 2.0, "hello"]
		Словари-dict - список пар ключ-значение
			{"john" : "+1-23-45", "bob": "+1-32-65"}
		Кортежи-tuple - неизменяемые объекты
			(1, 2.0, "hello")
		Множества-set - последовательность уникальных объектов
			{"a", "b"}
		Булевые значения-bool - логические значения
			true, false

12. Числа и элементарная математика
	
	#operations
	= + - * /

	# round a number
	round(3.4)

	#module
	3%2

	#stepen'
	2**38

13. Переменые

	#create a var
	x=3

	#type of var
	type(x)

	#math module
	import math

	#square with math
	math.sqrt(x)

14. bool и None

	#bool var
	a = True

	#equal check
	a==b
	out: True or False

	#create a bool
	x=2==2
	out:x=True

	#create None
	a = None

15. Тип string

	#new line
	print("Text \n text")
	out: Text
		 text

	#windowed lines
	print('C:\\Users\\EngineerSpock')

	#another way to windowed lines
	print(r'C:\Users\EngineerSpock')

	#create string
	x = str("text")

	#check for id
	x[0]
	out: 't'
	x[2]
	out: 'x'
	x[-2]
	out: 'x'
	x[2:] #start from index 3
	out: 'xt'
	x[0:3] #from 0 to 3(not included)
	out: 'te'
	x[::2] #each second index

	#concatenation !high memory
	"textio" + "textes"

	#placeholders !low memory
	print("%s %s" % (string1, string2))
	print("{} {}".format(string1, string2))

	#multiple string
	'a'*3
	out: 'aaa'

16. Функции string

	#length
	len(x)

	#count chars
	x.count('l')

	#first symbol in high, other in low register
	x.capitalize() #it is important(???) to write like that x.lower().capitalize() to receive 'Normallystring'
	x.title() #another way

	#all in high register
	x.upper()

	#all in low register
	x.lower()

	#check for register
	x.isupper()
	x.islower()

	#find char returns index
	x.find('l') #first founded symbol!
	x.find('l', 5, 10) #check from 5 to 10

	#replacing string
	#returns a copy of the string where all occurrences of a substring is replaced with another substring.
	string.replace(old, new, [count])

	#delete symbols
	string.replace('a', '') #it means we are deleting all 'a' letters from string
	#or, the same
	s.translate({ord('a'): None})

	#check for symbol type in string
	symbol.isdigit() #if number
	symbol.isalpha() #if letter

	#check for num !and letters! without punctuation chars
	x.isalnum()

	#check for empty string
	x.isspace() #without spaces too!

	#check for starting chars
	x.startswith("te")

	#split by char
	x.split('x')
	out: <class 'list'> ['te', 'tio']

	#participate
	x = "textio is cool"
	x.partition('is ')
	out: 'textio', 'is ', 'cool'

17. Форматирование строк

	#formation
	print("My name is {} and i'm {}".format("Alex", 22))
	print("Pi equals {pi:5.2f}".format(3.1415)) #5 chars before dot and 2 after
	print(f"My name is {name} and i'm {age}")
	print("Pi equals {pi:5.2f}")

18. Операторы сравнения

	#operators
	x>y
	X==y
	X!=y
	X>=y

19. Операции над файлами

	#check directory
	import os
	dirpath = os.getcwd

	#write file
	open('file_name', 'w') as file:
		file.write('data')

	#open file
	obj = open('file.txt')

	#read file
	obj = file.read() #make attention that cursor will move to the end of the file

	#for correct display
	print(obj)

	#move cursor
	#0 = byte offset 2 = byte start
	obj.seek(0, 2) # from the end
	obj.seek(0, 0) or obj.seek(0) #from the start
	obj.seek(0, 1)	#relatively from current position (use offset)

	!obj has a type = 'string'

	#read each line and create a list
	lines = obj.readlines()

	#make way to file
	sample = open(r'C:\\Users\\user\\sample.txt')

	#close file
	obj.closed()

	#operation with file in separated block
	with open('sample.txt') as sample_file: #file will automatically close when block ends
		obj = sample_file.read()

	File modes:
		'r' - read only(error if writing)
		'w' - write only (error if reading, overwrites existing file or creates new one)
		'a' - append only (error if reading or writing to inexistent file)
		'r+' - reading and writing (error if writing to inexistent file)
		'w+' - reading and writing (overwrites existing file or creates new one)

	"!"trying to read an inexistent file always leads to an error

	#set mode
	with open('sample.txt', mode = 'r') as sample_file:

	#finally, correct way to open file
	import os
	script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
	rel_path = "2091/data.txt"
	abs_file_path = os.path.join(script_dir, rel_path)

20. Строки и байты: str, bytes, bytearray
	
	#check encode type
	import sys
	sys.getdefaultencoding()

	#get char code
	ord(char)

	#get char
	chr(number)

	#check default type of encoding, returns string
	getdefaultencoding()

	#set type for encoding and decoding
	obj.encode('ascii') #if no args, encodes by default
	obj.decode('utf-8')

	#convert to bytes
	bytes(obj)

=
-----Раздел 3: Коллекции, циклы и логика в Python-----
=

24. list - список

	#create list
	obj = [1,2,3]

	#list len
	len(obj)

	#take all elements except num
	obj[num:]

	#concatenation
	lst1 + lst2 = lst[all elements lst1 and lst2]

	#append operation
	lst.append(element)

	#sorting
	lst.sort()

	#sort by key
	lst.sort(key=len)

	#reversing sort
	lst.sort(reverse=True)

	#reverse list, not sorting - just reverse
	lst.reverse()

	#insert element in current index
	lst.insert(index, element)

	#search index of element
	lst.index(element, start index, end index)

	#count all x in lst
	lst.count(x)

	#copy of list for another var
	lst.copy()

	#clear list
	lst.clear()

25. dict - словарь

	#create dict
	var = {'key': value, ...}

	#get value by key
	var.get(key)

	#len of dict
	len(var)

	#add a value
	var[key] = value

	#delete key
	del var[key]

	#another way to delete
	var.pop(key)

	#delete last item
	var.popitem()

	#get keys
	var.keys() #type dict_keys, but we can also convert it to list
	lst = list(var.keys()) #convert

	#get values
	var.values() #same logic (look above)

	#sorting by keys
	sorted(var.keys())

	#sorting by values
	sorted(var.values())

	#bool comparison
	boolvar = key in var

	#get pairs key-value
	var.items()

	#check all items in dict
	for k, v in var.items():
		print(k,v)

	#set new key
	var.setdefault(key)
	out: {..., key: None}

	"!"In dict we cant append an existing key! Dict never uses two keys with same name.

26. OrderedDict vs dict

	Для dict не важен порядок расположения ключ-значение. 
	Для OrderedDict важен этот порядок расположения.
	Это в целом влияет на булевы значения при сравнении словарей.

	#create ordered dict
	var = OrderedDict()

27. tuple - кортеж

	tuple - неизменяемый list. Зачастую содержат значения с определённым смыслом.

	#create tuple
	var = (x, y, z)

	"!"Операторы присваивания не поддерживаются кортежами.

	#len
	len(var)

	"!"tuple в основном поддерживает все значения list, которые не изменяют его.
                                    
28. namedtuple - именованные кортежи
	
	#import
	from collections import namedtuple

	#create namedtuple
	Player = namedtuple('Player', 'name age rating') #it is like a class with own parameters

	#create a list of tuples
	players = [Player('Carlsen', 1990, 2842), ...] #it is like an instances of class Player

	"!"Получаем инстанции класса Player с атрибутами, которые не можем изменить. Это и есть namedtuple.

	players[index] #get all instance
	players[index].value #get value

29. Логика с условиями

	#condition operators
	if, elif, else

	#input getter
	var = input()

30. set - множество

	#create set
	var = set()

	#add element
	var.add(x)

	"!"set contains only unique elements

	#bool check
	x in var

	#check by subset
	set1.issubset(set2) #all elements of set1 contains in set2

	#check by superset
	set1.issuperset(set2) #all elements of set2 contains in set1

	#check if set1 not contains elements of set2
	set1.isdisjoint(set2)

	#difference in elements between sets - return all absent in both sets elements
	set1.difference(set2) #all elements contains in set1 and don't have set2
	set1.symmetric_difference #all elements contains in set1 and don't have set2 AND contains in set2 and don't have set1

	#union of sets
	set1.union(set2) #returns a new set!

	#update - append elements from set2 to set1
	set1.update(set2) #doesn't return a new set like union!

	#intersection - all elements that contains set1 and set2
	set1.intersection(set2)

	#delete element
	set1.remove(x) #makes an error if set1 doesn't have x
	set1.discard(x) #doesn't make an error if set1 doesn't have x
	set1.pop() #delete and return a random element

	#clear set
	set1.clear()

31. Цикл for

	#syntax of for
	for i in var: #var have to be iterable
		/action

	#range - create a list with sequental numbers
	range(1,100) #last number(100) doesn't included
	range(5) #short syntax = range(0,5)

	#tuple unpacking
	var = [(x, y), ...] #list of tuples
	for x, y in var: #check x,y in all elements of list

	#dict unpacking
	for item in dictvar.items():
	out: tuples (key, value)
	for k,v in dictvar.items(): # unpacks a tuples with key and value
	for v in dictvar.values():

	#nested cycles
	for x in var1:
		for y in var2:

32. list comprehension

	#iteration in varStr
	for i in varStr: 
		varLst.append(i*2)

	#list comprehension
	varLst = [i*2 for i in varStr] #this action is the same as above
	"!"Взять каждый i из varStr, умножить на 2 и вернуть в переменную varLst

	#list comprehension with condition
	var = [i*i for i in range(0,11) if i%2!=0] #also we can put else branch
	"!"Взять каждый i из varStr, который подчинается условию i%2!=0, умножить на саму себя и вернуть в переменную var

33. Цикл while, continue, break

	#while syntax
	while var < i: #do action while condition is true
	else: #also we can put else branch

	continue #close current iteration and go to next iteration
	break #closing current cycle
	pass #just go to next action in same iteration

=
-----Раздел 4: Функции и модули-----
=

44. Помощь по функциям

	#func help
	help(func.action)

	#documentation Python
	docs.python.org

45. Встроенные функции

	#module
	abs(-1)

	#max number in list
	max(1,2,3,4,5)
	out: 5

	#in power
	pow(2, 8) # 2 in power 8

	#round
	round(3.37, 1) #1 - number of chars after dot

	#sum all numbers in list
	sum(list)

	#code systems
	hex(4)	#16
	oct(4)	#8
	bin(4)	#2

	#boolean all
	all(bool_list) #check if all elements are true
	all(rating > 2700 for _, rating in players) #check for rating in dict players

	#boolen any
	any(bool_list) #any of all elements are true

	#create an iterator
	zip(letters, numbers) #lazy evaluation - need a request
	list(zip(letters, numbers)) #need to make a list to get proper result

46. Основы функций

	#create function
	def func(arg1,arg2 ...):
		''' #function info, get with help(func)
		DOCSTRING: Info 
		INPUT: input
		OUTPUT: Hello!
		'''
		/action

	#default args
	def func(arg1='Default'): #arg1 will be 'Default' if it calls without arg'

	#finally, close func and return something to first caller
	return something

	#take any number of arguments
	def func(*args):
		for x in args: #with this func we can action any number of arguments
			/action 

	#take N number of pairs key-value
	def func(**kwargs):
		for k, v in kwargs.items(): #we can use any number of pairs and, for example, iterate it
			/action

	#we also can use two types and create func with *args and **kwargs
	def func(a,b,c,d,*args,**kwargs):
		/action

	"!"*args и **kwargs это условные понятия, но общепринятые, рекомендуется использовать именно такие наименования

47. Лямбды

	#map function that can use func on some iterable list
	map(func, *iterables) #func takes a values from iterables

	"!"Функция map применяет функцию к каждому элементу последовательности и возвращает итератор с результатами.

	"!" map - it is a lazy evaluation, we need to request it for results

	#request map
	for x in map(func,*iterable):
		action

	#greedy operator - all in one line
	list(map(func, iterable))

	#filter function - lazy evaluation
	filter(func_bool, iterable) #it is important to send function with boolean return
	#filter will return only those iterables that passed through func_bool with True return

	"!"Функция filter() применяет функцию ко всем элементам последовательности и возвращает итератор с теми объектами, для которых функция вернула True.

	#greedy filter
	list(filter(func_bool, iterable)) 

	#lambda create 
	var = lambda arguments: x>=y #only one statement
	#lambda is a short realization of def func(), but only for use in one place

	#greedy lambda in-place
	list(filter(lambda arguments: x>=y, iterable))

	48. Вложенные функции и область видимости переменных

	Types of vars:
		1. Built-in #standard vars built in python
		2. Global #global vars for all methods
		3. Enclosing local 
		4. Local

	#built in
	list, str, int

	#global var
	var = x #global var

	#local var
	def func():
		var = x #local var

	#enclosing var
	def func():
		var = x #enclosing local var
		def func2():
			var = x #local var

	"!"У каждой функции своя переменная и один тип переменной не может переписать стоящую выше.

	#make a global in func
	def func():
		global var #use global var in func body

49. Декораторы

	#call inner func in main func
	def func():
		def func_inner():
			/action
		return func_inner

	#use function as an argument
	def func_main(func_sub):
		/action

	"!" Декораторы - содержат в себе wrapper - обёртку

	#use a decorator - it will be an action shell for argument func
	def func_decorator(func):
		def wrap():
			/action #shell
			func()  #argument function
			/action #shell
		return wrap

	#we can use above decorator to function like this
	@func_decorator
	def func():
		/action

50. Декоратор @wraps
	
	"!"Обычные вызовы декораторов осложняют отладку так как первоначальная функция, к которой применяется декоратор,
	при вызове help(func) именуется как wrapper. Лучше делать именно с @wraps как в примере ниже. 

	from functools import wraps

	#use @wraps in standard decorator
	def func_decorator(func):
		@wraps(func) #call wraps decorator
		def wrap():
			/action #shell
			result = func()  #argument function
			/action #shell
			return result #need to return func if it returns something inside yourself
		return wrap

	#call wrapper
	@func_decorator
	def my_main_func():
		/action

=
-----Раздел 5: Ошибки и исключения. Автоматизированные тесты-----sprinkle
=

55. Основы обработки ошибок

	#errors catching
	def func():
		try: #block with main action
			return something
		except NameError as ex: #block that catches error with same name-> 
		#->and writes it to var ex and does some action with it
			/action with {ex}
		#general except block
		except: #block for error with any name
			/action
		else: #it runs if programm didn't throw an any exception
			/action
		finally: #this block calls in any situation after all except blocks
			/action 

56. Выброс исключений. Кастомные типы исключений.
	
	#custom exception type
	class MyNameError(Exception): #class-children of class Exception with custom name

	#call an error by name
	raise MyNameError('error info')

57. Основы юнит-тестирования

	#import testing unit
	import unittest

	#create a result of function's work and write it to new variable 'result'
	result = NameClass.get_reply(var)
	#check if the function should to return refult 'Fizz'
	self.assertEqual(result,'Fizz')

	#check if we call function directly
	if __name__ == '__main__':
		unittest.main()

=
-----Раздел 6: ООП в Python-----
=

58. Основы классов

	#create class
	class Character():
		pass

	#instance of class
	unit = Character()

	#constructor of class
	def _init_(self, race): #function that will assign a new value of arg race to instance of class
	#initialization function that takes self - reference to class, and some arg race
		self.race = race #for the instance of class we write arg class

	#instance of class with init
	unit = (Character("Elf"))

59. Атрибуты и методы

	#adding parameters to class
	class Character():
		max_speed = 100 #parameters that will receive a new instance
		dead_health = 0
		def __init__(self, args....):
			self.health = 100 #we can add parameters whenever of received args

60. Константы. Защищённые и приватные атрибуты. Свойства.

	#create a constant
	MAX_SPEED = 100 #constant with caps defending yourself from random changing

	#private parameter
	__var #python will block any external change of this var
	Character.__var #will not work!

	#defended parameter
	_var #we can access but _ signalize that we need to be careful!

	#create properties of class
	@property #property can give access to read vars of the instances
	#this is not an access to re-write var! just for reading!
	def func(self):
		return self._var

	#property setter
	@var.setter
	def var(self, var) #way to re-write defended var
	if var < 100: #if we correctly input var, func will change defended var
		_var = 0

61. Статические методы - @staticmethod, @classmethod

	"!"Атрибуты стандартного класса принадлежат самому классу и ОТДЕЛЬНО его инстанциям. Т.е изменяя параметр инстанции
	параметр самого класса не изменяется.

	#create class method
	@classmethod
	def func(cls, var1, var2...) #cls - info about class where method staying
		return cls(var1, var2...) #call class __init__ constructor

	#create static method
	@staticmethod
	def func(var1, var2):
		return MyClass(var1, var2...) #call class __init__ constructor

	"!"Статический метод вызывает конструктор класса MyClass, но если его использовать в наследниках этого класса, то он
	будет также вызывать ТОТ ЖЕ экземпляр родителя.
	У метода класса будет вызываться конструктор того класса, из которого вызван.

	Статический метод АБСТРАГИРОВАН от класса.


62. Наследование и полиморфизм

	#inherit class
	class NewClass(FirstClass): #NewClass inherits FirstClass parameters and methods
		def same_def(): #we can re-write parent's methods in children class

	"!"Если несколько классов реализуют один и тот же метод python это учитывает, 
	и мы можем использовать концепцию полиморфизма.


63. Множественное наследование

	#several inherits
	class NewClass(FirstClass, SecondClass): #NewClass takes methods from First and Second classes

	"!"Deathly Diamond of Death - при наследовании класса из двух других, у которых есть одинаковые методы, при вызове
	метода из нового класса, будет учтён порядок наследования(у первого по наследованию будет вызван метод).
	А если ещё у самого нового метода-наследника вызвать такой же метод, то переназначаться будут все родители по
	двойной иницилизации.

	#function super()
	super().method(self, var) #fixing a problem with double initialization
	#that will simply use all parent's method actions

64. Миксины

	- we can add a new function to inherit of main class without adding at inherit itself with Mixin
	class RadioMixin: #mixin
		Radio()
	class Radio:

	class Car(Vehicle, RadioMixin): #use mixin to class Car, inheritance of class Vehicle

65. Абстрактный класс и модуль ABC

	#example of raising error in abstract class without 'abc module'
	class Fruit:
		def check_ripeness(self):
        	raise NotImplementedError("check_ripeness method not implemented!")

    class Apple(Fruit):
    	pass #we didn't re-write avstract class

	a = Apple()
	a.check_ripeness() # raises NotImplementedError because we didn't re-write an abstract class

	#import code that need to use abstract classes
	from abs import ABC
	from abs import abstractmethod

	#request to parent
	def __init__(self):
		super().__init__() #use parent initialization that will simply use all parent's method actions

	#abstractmethod - inheritant must to re-write these methods
	@abstractmethod #we can't create instance of inherit of abstract class where not all abstract methods are re-writed
	def perimeter(self):

	#//
	class Parent():
		def method_abc():
			/action
	class Inherit(Parent):
		def method_abc():
			super().method_abc() #with super we can easily re-write abstract methods

66. Магические методы

	def __str__(self): #string reveal of class for functions like a print()
		#that will incorporate in print() if we call any instance of this function in it
		return f'Class x={self.x}, y={self.y}' 

	def __del__(self): #method that will call if an instance has deleted
		/action

	x = Class(arg)
	del x #will cause /action from method __del__ of Class
	
=
-----Раздел 7: Модули и пакеты-----
=

72. PyPi и Pip

#site with moduls
- pypi.org

#launch
pip install modulename #write in command prompt

#import
from modulename import FuncName

73. Модули и пакеты

	Модуль - скрипт с расширением .py
		* создаём файл и пишем код, тут всё просто

	Пакет - набор модулей
		* создаём структуру каталогов с модулями внутри
		* в каждой папке структуры должен быть файл __init__.py

	Мы можем импортировать конкретную функцию с помощью from... import и не писать в коде modulename.func(), 
	а вместо этого func()

	Необходимо использовать путь Folder1.Folder2.TargetFolder
	Folder1 должна находится в той же директории что и автор вызова

	#give a new name
	from modulename import FuncName as MyName #MyName now compiling as a ClassName

	#import all functions from modulename
	from modulename import *

74. Ещё раз о __name__ и __main__

	#check __name__
	if __name__ == '__main__': #if this script will be launched directly
	#else it was imported (not executed directly)

=
-----Раздел 8: Дополнительно-----
=

75. Отладка

	#fixing module
	import pdb

	#stop point
	pdb.set_trace() #here pdb will stop

	"!"В точки остановки можно проверить переменные передавая их имена в строку pdb.

	/in pdb:
	#to next breakpoint
	c
	#quit
	q

76. Реализуем Stack

	"!"Стэк это list где существует правило - последним пришёл, первым ушёл.

	#python iterator object must implement two special methods - called iterator protocol
	def __iter__(self): #returns the iterator object itself. If required, some initialization can be performed.
		self.n = 0 #self counter for __next__ method
	    return self
	def __next__(self): #must return the next item in the sequence
	    if self.n <= self.max:
	        result = 2 ** self.n #do some needed actions with result
	        self.n += 1 #add counter
	        return result
	    else:
	        raise StopIteration() #special exception

	"!"An object is called iterable if we can get an iterator from it.

77. datetime - даты и время

	#import datetime modules
	from datetime import datetime
	from datetime import date
	from datetime import time
	from datetime import timedelta

	#create date object
	d1 = date(2019, 3, 12)

	#create time object
	t1 = time(23, 10, 59)

	#date according to computer settings
	date.today()

	#mixed object
	dt = datetime(2019, 3, 12, 15, 17)
	out: 2019-03-12 15:17:00

	#check min and max existing values
	datetime.max
	datetime.min

	#datetime according to computer settings
	dt = datetime.now()

	#we can also return each element of datetime
	dt.year
	dt.month

	#replacing
	dt_replaced = dt.replace(year=2018) #copy dt with replaced year and save it to dt_replaced (dt will not change!)

	#parse datetime
	dt.strptime("29/03/2018 10:40", "%d/%m/%y %H:%M")

	#set display format
	print(st.strftime('%Y-%m-%d (%a)')) #we are using built-in placeholders

		Формат	Значение
	%a	название дня недели в сокращенном виде
	%A	название дня недели в полном виде
	%w	номер дня недели в виде целого числа
	%d	номер дня месяца в виде целого числа
	%b	название месяца в сокращенном виде
	%B	название месяца в полном виде
	%m	номер месяца в числовом представлении
	%y	номер года без столетия
	%Y	номер года в полном представлении
	%H	количество часов в 24-часовом формате
	%I	количество часов в 12-часовом формате
	%p	до полудня или после полудня в 12-часовом формате
	%M	количество минут в виде целого числа
	%S	количество секунд в виде целого числа
	%f	количество микросекунд в виде целого числа
	%z	часовой пояс в формате UTC
	%Z	название часового пояса
	%j	номер дня в году
	%U	номер недели в году, если считать с воскресенья
	%w	номер недели в году, если считать с понедельника
	%c	местное представление даты и времени
	%x	местное представление даты
	%X	местное представление времени
	%%	символ процента

78. Singleton Design Pattern: __new__ и __init__

	#constructor
	def __init__(self): #with that we are constructing class

	#__new__ method saves new instance of object in memory
	def __new__(cls):
		obj = super().__new__(cls) #request to current object
		return obj

	"!" __new__ - это метод который позволяет выделить блок в памяти для экземпляра класса, тем самым обращаясь
	к самому объекту, в то время как __init__ просто осуществляет инициализацию.
	По сути, объявленное выше представление __new__ автоматически происходит каждый раз, когда вызывается новый
	экземпляр класса и вызывается он ПЕРЕД __init__.

	"!" Pattern - шаблон класса
	Singleton Pattern - шаблон класса-одиночки, в котором может быть вызван лишь один экземпляр класса.

	#singleton pattern
	class MySingleClass():
		_instance = None

		def __new__(cls): #we must send requests with cls. prefix because we are alwas working with class object
			if not cls._instance:
				cls._instance = super().__new__(cls)
			return cls._instance

	"!" Сколько бы инстанций мы бы не создавали - всегда будет возвращатся лишь одна, которая была создана изначально
	и является единственной для всех экземпляров класса.

79. Pickle - консервирование

	import pickle

	#canning into file - pickling
	pickle.dump(class_instance, file)

	#load canned file - unpickling
	pickle.load(file) #with that __init__ won't call again, all changes in the origin class will not affect it

	#__setstate__ and __getstate__
	class MyClass:
		def _setstate_(self, state): #what will be uncanned - we can also set new parameters - if class contains them
			#state - its file data
			self.race = state.get('race', 'Elf') #it means get from the state
			self.armor = state.get('armor', 20)
		def _getstate_(self): #we kchoose what exactly will be canned  	

80. repr and str, eq and ne, eval

	#print in string view - returns reproducable string - we can use it in another function
	repr(lst) #dunder method __repr__
	out: '[1, 2, 3]'

	def __repr__(self):
		return f"Character('{self.race}', {self.damage})"

	#print in informational view - we can't use it further
	print(lst) #dunder method __str__
	out: [1, 2, 3]

	def __str__(self):
		return f'{self.race} with damage = {self.damage}'

	#evaluate - returns True or False
	eval(repr(lst)) == lst

//////
	 EVAL
Разбирает и исполняет указанное выражение.

---> eval(expression, globals=None, locals=None) -> Результат выполненного выражения

expression : Выражение, которое требуется исполнить, в виде строки. Либо объект кода.
globals=None : Ожидается dict. Словарь глобального пространства, относительно которого следует исполнить выражение. 
Если указан, но не содержит атрибута __builtins__ данные указанного пространства будут дополнены данными общего 
глобального пространства, перед разбором выражения. Таким образом, выражение будет иметь доступ ко всем встроенным 
модулям.
locals=None : Ожидается объект-отображение (например, dict). 
Локальное пространство, в котором следует исполнить выражение. Если не указано, то используется словарь 
глобального пространства.
//////

	#dunder method __eq__ - its needs for equal comparison
	def __eq__(self, other):
		if isinstance(other, Character):
			#in this case we compare races and damages
			return self.race == other.race and self.damage == other.damage #returns bool
		return False

	#dunder method __ne__ - its needs for non-equal comparison
	def __ne__(self, other): #its not necessary because in most cases you can only present __eq__
		#you need __ne__ actions if you want to create new specific action for non-equal comparison
		/action

81. Deep copy vs Shallow copy

	# shallow copy
	// 
	list1 = [1, 2, 3, [4, 5, 6]]
	copied_list = list1.copy()
	copied_list[3].append(7)

	"!" 7 будет добавлена в ОБА списка (изначальный и скопированный), так как метод list1.copy() создаёт так называемое -
	- неглубокое копирование (Shallow Copy). Т.е два этих объекта имеют один и тот же массив в памяти на индексе 3 - 
	- [4, 5, 6]
	Иными словами при Shallow Copy просходит поверхностное копирование, а на все составные части элемента копируются лишь
	ссылки.

	#deep copy
	deep_copy = copy.deepcopy(list1)

	"!" Deep Copy, наоборот, проходит рекурсивно вглубь объекта и копирует также все составные части.

	#dunder method __copy__
	def __copy__(self):
		cls = self.__class__ #get info about class
		result = cls.__new__(cls) #create a new instance
		result.__dict__.update(self.__dict__) #update new instance with current values
		return result

	#dunder method __deepcopy__
	def __deepcopy__(self, memo):
		cls = self.__class__ #create a new instance
		result = cls.__new__(cls) #update new instance with current values
		memo[id(self)] = result #find an id of object and put there our new instance

		for k, v in self.__dict__.items():
			setattr(result, k, copy.deepcopy(v, memo))

		return result

//////
	 OBJECT.__DEEPCOPY__
Позволяет определить действие при глубоком копировании экземпляра.
object.__deepcopy__(self, memo) -> копия экземпляра
self : Ссылка на экземпляр.

memo : Словарь для реконструкции графа объектов.
Данный метод позволяет переопределить поведение при попытке применения функции deepcopy() из модуля copy, 
производящей глубокое копирование, к экземпляру класса.

Внимание
Реализация должна создавать глубокую копию объекта. Для этого ей следует вызвать copy.deepcopy(), 
где первый аргумент — это сам объект, а второй — словарь для реконструкции графов сложных объектов 
(словарь должен хранить соотношения идентификаторов объектов к объектам-копиям).

from copy import deepcopy

class MyClass:

    def __init__(self):
        # Допустим в some_attr сложный объект, включающий в себя другие объекты.
        self.some_attr = ...

    def __deepcopy__(self, memo):
        print('deep copying ...')
        my_copy = type(self)()
        memo[id(self)] = my_copy
        my_copy.some_attr = deepcopy(self.some_attr, memo)
        return my_copy


my_object = MyClass()
my_object_copy = deepcopy(my_object)  # deep copying ...
//////

82. Enum - перечисления

	"!" Enumeration - перечисление набора констант. Модуль enum позволяет с ними работать.

	from enum import Enum #all objects
	from enum import IntEnum #int with arithmetic comparisons
	from enum import IntFlag #flags with boolen comparisons

	#Enum inheritance
	class TrafficLight(Enum):
		#vars can contain any objects - not only numbers! 
		RED = 1
		YELLOW = 2
		GREEN = 3

	#calling
	TrafficLight.RED
	out:<TrafficLight.RED: 1>

	TrafficLight(1)
	out:<TrafficLight.RED: 1>

	TrafficLight['RED']
	out:<TrafficLight.RED: 1>

	TrafficLight.RED.value
	out: 1

	#iterate
	for c in TrafficLight:	

83. Работаем с JSON

	"!"JSON - формат для передачи данных между различными системами.

	#module for working with json
	import json

	#definite class
	class Tournament:

		def __init__(self, name, year):
			self.name = name
			self.year = year

	#definite dictionary
	tournaments = {
		"Aeroflot Open": 2010,
		"FIDE World Cup": 2018,
		"FIDE Grand Prix": 2016
	}

	#compare to json format
	json_data = json.dumps(tournaments) #serialization - process of comparing to json

	#compare to current format
	loaded = json.loads(json_data) #deserialization - process of comparing back to programm

	"!"Кастомные объекты по умолчанию не являются сериализуемыми в JSON. 
	В Python только примитивы можно по-умолчанию сериализовать.
	Как сделать кастомный объект(напр. инстанцию класса) сериализуемым? --->

	--->#serialize an instance of class
	json_data = json.dumps(instance_of_class.__dict__)

	#deserialization an instance of class
	instance = MyClass(**json.load(json_data)) #MyClass will receive to __init__ values from json_data

	#serialization into file
	with open("player.json", "w") as file:
		json.dump(my_object, file, default=lambda obj: obj.__dict__) 
		#default=lambda obj: obj.__dict__ --> its for deeping serialization

	#deserialization from file
	with open("player.json", "r") as read_file:
		data = json.load(read_file)

84. Генераторы

	#create generator
	def randoms(min, max, n):
		for i in range(n): #it means for each iteration generator will create result "in place"
			yield random.randint(min, max) #== return generator - yield is like analog for return
	randoms(1, 10, 10) #will return generator object

	"!"Генератор(*) не хранит значение в памяти, он генерирует их на лету. 
	* применяется лишь единожды в одном направлении.
	* позволяет генерировать результат в режиме lazy evaluation в данном случае только по мере прохождения циклом.
	@Все генераторы являются итераторами@ но @не все итераторы являются генераторами@
	Генераторы - содержать в себе один или несколько yield.
	Итераторы - как правило, содержат return.
	Это полезно, если цикл может выйти на какой-либо итерации (последующие итерации не будут сгенерированы).

	Yield это ключевое слово, которое используется примерно как return — отличие в том, что функция вернёт генератор.

	#module for iteration
	import itertools

	#method for different number generations in runtime
	itertools.islice(random_sequence_generator, 5) #5 - number of generations

	"!"Одна из концепций для генераторов - создания бесконечных ничем не ограниченных генераторов - 
	- (они ведь всё равно не сохраняются в памяти, а вычисляются в момент вызова!), а затем ограничение их
	работы при вызове (напр. методом itertools.islice)

	#alternate way to take new iteration from generator
	n = next(my_generator)

	#generator expression
	my_generator = (x**2 for x in my_list) #() gives it "in place" logic

85. Модуль itertools

	#module for iteration
	import itertools as it

	"!"Следует различать понятия объекта-итератора и итерируемого объекта. 
	Итератор это объект, который используется для итерации по итерируемому объекту, используя dunder-метод __next__().

	Справедливо следующее утверждение: любой объект-итератор итерируем, но не любой итерируемый объект ...
	... является объектом-итератором.
	Например, list итерируем, но сам по себе итератором не является. Чтобы получить итератор из итерируемого ...
	... объекта, надо воспользоваться методом iter(), который, собственно, и возвращает объект-итератор.

	#call __iter__ method for iterable
	iterator = iter(iterable)

	#then, call __next__ method
	next(iterator)

	"!"itertools построен на генераторах(а они все являются итераторами).

	#generate even numbers 
	even_numbers = it.count(start = 0, step = 2) #analog [x for x in range(10) if x%2 == 0]

	#repeat a value several times
	it.repeat(number_to_repeat = 1, times = 5)

	#endless cycle
	it.cycle([1, -1])
	out: 1, -1, 1, -1, 1, -1 ...

	#arithmetic sequence
	it.accumulate([1, 2, 3, 4])
	out: [1, 3, 6, 10]

	#comparing each pairs and return maximum on origin position
	it.accumulate(lst, max)

	"!"We can throw custom function in accumulate.

	#chaining elements in list, returns chained-elements list
	it.chain.from_iterable(['ABC', 'DEF'])
	out: ['A', 'B', 'C', 'D', 'E', 'F']

	#составить зип для словаря из имён(ключ) и рейтинга(значение), но эта функция будет также добавлять, в отличии ...
	#... от оригинального зипа ключи без значений(если нужно дефолт можно также задать(см.пример))
	it.zip_longest(names, ratings, default_value = 0)

	@COMBINATIONS
	#let's imagine that our pin contains these numbers, but we don't remember proper sequence of them
	pin = [7, 5, 2, 8]
	#we can get list of all existing permutations with this origin list
	it.permutations(pin)
	@

	#generate product stack
	#имея два списка листов(например лист мастей и лист карт) - мы можем сгенерировать все возможные соответствия ...
	#таким образом получив колоду карт. Короче говоря, простое перемножение двух листов.
	it.product(lst1, lst2)

	#check for all combinations
	it.combinations(lst, number_of_elements = 2) #скомбинировать все возможные комбинации из элементов листа

	"!"Если по генератору нужно пройтись несколько раз (и это нельзя совместить), лучше сразу его упаковать в list.

86. Интроспекция

	"!"Интроспекция - анализ собственных объектов

	#call dunder doc
	print(issubclass.__doc__)
	#same
	help(issubclass)

	#can we call object or not
	callable(obj)
	#ex.
	=callable(print)
	->True
	=callable(circle)
	->False

	#return all attributes (including dunders)
	dir(obj)

	#returns system string of object for debugging
	repr(obj)

87. Модуль requests

	import requests

	#send request
	requests.get("https://www.google.com/")
	--> <Response [200]> # 200 = special https code

	#raise error if inexistent url
	requests.raise_for_status()

	#we can parse for content, headers, etc.
	response = requests.get("https://www.google.com/")
	response.content
	responce.headers

	#we can also set parameters to get
	requests.get("https://www.google.com/", params = b'postId=1') #will return all elements with postId = 1

	#we can post our json data to https url
	requests.post("https://httpsbin.org/post", json = json_data)

	#getpass function for password request in authentification
	from getpass import getpass
	requests.get("https://api.github.com/user", auth = ("MyLogin", getpass()))
	--> @-input field for your password-@

	#timeout
	from requests.exceptions import Timeout

	try:
		response = requests.get("https://www.google.com", timeout = 1)
	except Timeout: #if we are waiting longer than one second (timeout = 1)
		pass

	#session work with connections
	with requests.Session() as session:
		session.auth = ('MyLogin', getpass())
		response = session.get("https://api.github.com/user")
		#we can work with same connection in the same "with" module and do not create many requests
		#better way to do like this

	#use adapter in requests
	from requests.adapters import HTTPAdapter

	adapter = HTTPAdapter(max_retries = 3)
	with requests.Session() as session:
		#we can use adapter and take sure that we will have at least 3 attempts
		session.mount('https://api.github.com/', adapter)
		...

88. Управление памятью

	- Память распределяется на стек и кучу.
	- Имена связываются с объектами в куче.
	- Ссылки = имя указывающее на объект в куче
	- Один объект может помечен множеством меток == имён
	- Если у объекта нет метки, то приходит злой сборщик мусора

=
-----Раздел 9: Движемся дальше-----
=

89. Введение в Линтеры

	"!"Readability and maintainability

	Lint - стилистические потенциальные баги из-за нелогичных условий или нелогичных передач аргументов
	Linter - автоматизированные инструменты, проверяющие код на стилистические и логические ошибки.

90. Установка системного Python

	<-->

91. Виртуальное окружение

	Системы окружений:
	- venv
	- pipenv
	- conda

	cmd:
	= python -m venv venv-test
	-> creating venv environment

	= \activate.bat
	-> activate environment

	= \deactivate
	-> deactivate environment

92. Установка PyCharm

	<-->

93. Создаём проект в PyCharm

	<-->

94. Refactoring, Quick Fixes, Debugging в PyCharm

	<-->

95. Type Hints

	#create expected type of variable
	def method(self, armor: int, power: int)

	#create expected type, but we also can give None to variable
	from typing import Optional
	variable: Optional[int]

	#all types
	from typing import Any
	variable: Any

	#will expect one of given types
	from typing import Union
	variable: Union[int, float]

	#define what types list can contain
	from typing import List
	variable: List[int]

	#define what types tuple can contain
	from typing import Tuple
	variable: Tuple[str, int]
	#many objects of one type
	variableL Tuple[int, ...]

	#same with dictionary
	from typing import Dictionary
	variable: Dict[str, int]

	#define that kind of object method will return
	def method() -> Iterable[int]:

	*PEP 484 - Type Hints
	*HABR - https://habr.com/ru/company/lamoda/blog/432656/ - about Type Hints

96. Введение в dataclasses

	@Data Transfer objects
	Using for creating class with only __init__ method, they are containing only variables and no operations.

	#define dataclass - only have variables, we can use it instead namedtuples
	@dataclass(frozen = True) #if frozen == True, after creating instance, we can't change it
	class Question:
		#all variables must have type hints
		text: str
		is_true: bool
		explanation: str

	*HABR - https://habr.com/ru/post/415829/ - Data Classes

=
-----Раздел 9: Движемся дальше-----
=

97. Обзор нововведений

	- Синтаксический сахар: walrus-operator
	- Навязывание позиционных аргументов
	- Перегрузка методов @overload
	- Новые type hints
	- Отладка с интерполированными строками
	- Различные оптимизации
	- Dangerous syntax warnings

98. Устанавливаем Python 3.8 и создаём проект

	<-->

99. Walrus-оператор

	#initialization + operation in one line
	print(walrus := True) # := looks like a walrus :D

100. Навязывание позиционных аргументов

	#imposing position arguments
	def avg(a, b, c, /, non_position_arg1, arg2 ...): #before / we must use position calling
	#ex.
	avg(1, 2, 3, arg1 = 'test', arg2 = 'test') #we can
	avg(a = 1, b = 2, c = 3, arg1 = 'test', arg2 = 'test') #we can't (we use position arguments only /)

	#keyword arguments
	def copy(*, source, destination, overwrite): #all args after * are keyword arguments
	#ex.	
	#only proper way to use keyword args (opposite to position arguments)
	copy(source = 'test', destination = 'test', overwite = True)

101. Улучшения в системе type hints

	#we can limit what literals we can receive in method via list expression
	from typing import Literal
	def open(file, mode: Literal['r', 'w'])

	#new way to initialize constants
	from typing import Final
	pi: Final = 3.14

	#we can't inherit and change this class
	@final
	class Dog:

	#typeddict - we can prevent operations with inexistent objects in dict
	from typing import TypedDict
	class WordStat(TypedDict):
		word: str
		count: str
		comment: str
	#now we can define new instance of our class WordStat
	dict_result: WordStat = {....} #here we can't operate with inexistent keys

102. Перегрузка с @overload

	#we can use @overload for define different types of hints for methods
	@overload
	def add(some hints for some consequences):
	#
	@overload
	def add(some another hints for another consequences):
	#main function
	def add():

103. Duck Typing и протоколы

	#initialize protocol to avoid Duck Typing errors - like a calling inexistent method of the class
	class Flyable(Protocol):
		def fly(self):
	#make method to follow Flyable protocol instructions
	def process_flyables(flyables: List[Flyable]):

104. Упрощённый вывод значений в интерполированных строках

	#we can fastly print formatted objects with short write
	#ex.
	full_name = "Titan Pinkman"
	#instead of
	print(f'full_name={full_name}')
	#we can use
	print(f'{full_name=}') #out: full_name=Titan Pinkman

	#also we can equalize line space
	print(f'{full_name=:>15}') #15 == 'full_name=' length + spaces to variable value
	#out: full_name=     John Fowler

=
-----Раздел 11: Финальная практика-----
=

There are only exercises, so lets move next.

=
-----Раздел 12: Допматериалы-1. Введение в многопоточное программирование-----
=

113. Терминология

	- Параллельность: Parallel (computing)
	- Конкурентность: Concurrency
	- Многопоточность: Multithreading
	- Асинхронность: Asynchrony

114. Процессы и потоки

	Процесс = специальный контейнер-хостер программ.

	Поток исполнения = объект с набором последовательных программных инструкций.

	Поток = часть процесса (.exe в Windows)

	time-slicing = Так работает Python. Дробит задачу на много мелких подзадач и ОДНИМ ядром выполняет их.
					Но переключение имеет стоимость и последовательное исполнение на одноядерной машине всё-таки быстрее.

115. Виды процессинга

	- CPU-bound = операции, которые требуют исключительно процессорного времени

	- I/O-bound = операции, которые привязаны к медленным устройствам - дискам, сети и т.д

	- Для CPU-bound используется вытесняющая многозадачность (Windows, Linux) 
		ОС сама принимает решение по переключению задач

	- Для Input/Output-bound используется кооперативная многозадачность (когда вызов не блокирует вызывающий поток,
		а по завершению оповещает его об окончании). Потоки помогают друг другу.

	-------------------------------------------------------------------------
	| Вид процессинга | Как осуществляется | Параллелизация | Модуль Python |
	=========================================================================
	| 	CPU-bound	  | Переключение между |				|				|
	| (concurrency)	  | потоками через     |  Нет / 1 ядро  |	threading	|
	|				  |	time-slicing       |				|				|
	-------------------------------------------------------------------------
	| 	CPU-bound	  | Одновременное ис-  |				|				|
	|(parallelization)| -полнение N-пото-  |  Да / N ядер   |multiprocessing|
	|				  | -ков (задач)       |				|				|
	-------------------------------------------------------------------------
	| 		          | 	               |				|				|
	|   I/O-bound     |    Кооперация      |  Нет / 1 ядро  |	 asyncio	|
	|				  |	                   |                |				|
	-------------------------------------------------------------------------

116. GIL

	GIL - Global Interpreter Lock 
		->  Это булевая переменная, к которой поток должен получить доступ, прежде чем начать исполнение.
			Только один поток может иметь доступ к GIL в любой момент времени.
			Один GIL на процесс

=
-----Раздел 13: Допматериалы-1. Модуль Threading-----
=

117. Однопоточность. Демо проблемы

	-   Если один обработчик "застрял" в приложении с пользовательским интерфейсом.
		То процесс будет ожидать его и не сможет принять другие команды.
		Это порождает зависание и даже закрытие программы операционной системе.
		Это решается разделением потоками.

118. Foreground & Background потоки

	import threading

	Потоки:
		- Foreground 
		- Background (daemon)   #если форграунд завершён, все бэки закрываются автоматически! (если нет команды join())
								#это помогает, если обработчик работает неожиданно медленно, чтобы его закрыть
	
	"!" Пока пользователь взаимодействует с Foreground-потоком, Background выполняет функции.

	#daemon thread
	t = Thread(target, daemon=True) #target == operation which will define this thread
	#thread start
	t.start()
	#will wait for ending of thread t
	t.join()

119. "Параллельное" исполнение против последовательного

	"!" Потоки используются в основном для освобождения main loop.

	"!" Последовательное исполнение на одном ядре работает быстрее параллельного!
		Потому что переключение между процессами тоже стоит ресурса ядра.


120. Executor API

	"!" Создание потоков через Thread.start() довольно затратно. Поэтому необходимо использовать готовый пул потоков.

	concurent.futures - package with high-level types

	#threads pull executor
	ThreadPoolExecutor(max_workers = None)  #max_workers == numbjer of threads which will work on process
											#calculating logic if None: max_workers = number_of_shells + 4

	#parallel pull executor
	ProcessPoolExecutor(max_workers = None)	#max_workers == numbjer of threads which will work on parallel processes
											#calculating logic if None: max_workers = number_of_shells

	"!"Executor - абстрактный класс.

	#define executor with arguments to run function
	submit(func_to_evaluate, *args, *kwargs) 
	-> type: Future
	#Future - специализированный низкоуровневый тип, представляющий будущий результат асинхронного вызова функции.

	#when we need some submit() of the SAME function - we can use map()
	#plan to stand func as much as need depending on number of given arguments
	map(func_to_evaluate, *iterables, timeout = None, chunksize = 1) 
	#if timeout depended, returns TimeoutError if func staying more than timeout time
	#if we use ProcessPoolExecutor, chunksize will cut iterables into pieces and submit it into pull as individual tasks
	-> type: list []

	#closes executor with resource cleaning
	shutdown(wait=True) #if wait == True, shutdown will block thread until other thread will finish its work

121. submit-демо

	#-> True == Future is running
	Future.running()
	-> bool

	#-> result of Future
	Future.result()
	-> any type, depends on called to executor function

122. map-демо

	<-->

123. Синхронизация потоков

	Проблемы многопоточки:

	- Race
		> When threads are using the same global cariable and changing it in random sequence. Threads disturb each other

		- Problem solvers:
			import threading
			> Lock - unique access to resource, other threads cant access simultaneously
			> RLock - same as Lock, but thread can make reentrance
			> Event - one thread can wait for signal from other thread
			> Condition - union of Event and Lock
			> Semaphore - limits access to resource with number of threads
			> BoundedSemaphore - defends from "release"(bug function which adding new thread if old one have released)
			> Barrier - wait for ending of N-number of threads

	- Deadlock - infinitive each side blocking
		> infinitive waiting for unblocking two locks on one thread

		- Problem solvers:
			> proper structure of multithreading
			> set timeouts on lock
			> using RLock on recursive functions
			> other complicated ways to detect and avoid deadlocks

124. Гонка и Lock

	#locking action from racing between threads
	lock_obj = threading.Lock()
	#in with block can join only ONE thread simultaneously
	with lock_obj:
		/actions
	#or we can instead of "with:" use built-in Lock() functions
	lock_obj.acquire()
	/actions
	loack_obj.release()

125. Deadlock

	"!"Example scheme:
		Thread 1 --locks--> Resource A
				--waits--> Resource B

		Thread 2 --locks--> Resource B
				--waits--> Resource A

126. Демо дэдлока

	<-->

127. Синхронизация сигналами

	Проблема:
		- библиотека отвечает асинхронно - нужно сделать обёртку дающую возможность клиентскому коду, 
		по желанию дожидаться окончания операции

128. Применяем Event

	Event - это класс, через который можно управлять логикой программы, отправляя сигналы между её блоками.
			Это полезно, если мы не можем напрямую управлять одним из блоков.

129. Семафор

	Семафор - 	ограничение доступа к ресурсу по количеству потоков.

 	import threading

	#class Semaphore initialization
	Semaphore(value) #value == volume of semaphore

	#capture slot
	Semaphore.acquire()

	#release slot
	Semaphore.release()

	#return value
	Semaphore._value

130. Моделируем ночной клуб семафором

	С помощью семафора, мы можем, к примеру, ограничить потоки посетителей в наш "ночной клуб" до значения,
			передаваемого в класс Семафора.

131. Барьер

	Барьер - синхронизация фаз алгоритма, в котором задействованы N-потоков.
			 Т.е ожидание пока все потоки не завершает какое-либо действие (фазу)
			 Для потоков, успевших первее остальных завершить фазу, ставится барьер, предотвращающий дальнейшие действия.

	import threading

	#barrier initialization
	Barrier(parties) #parties == number of synchronized threads

	#set barrier
	Barrier.wait() #if barrier calls by this function parties-number times, barrier will be removed
	#but first call of this function will set barrier and stop thread at this line until other threads reach it

	#back to origin state
	Barrier.reset()

	#change to broken state
	Barrier.abort() #if barrier broken, we can't use it further

	#return number of threads which finished current phase and waiting
	Barrier.n_waiting

	#return state flag
	Barrier.broken

132. Атомические операции

	Атомарные операция - операция, которая выполняется целиком.
	Интерпретатор переключает потоки только между инструкциями байткода. Инструкции байткода неделимы.

	Атомарные операции - это операции которые состоят из двух действий.

	Пример:
	| L.append(x) #atomar operation (just append) == evaluating in one step
	----
	| i = i + 1 #non-atomar operation (calculating + assignment) == evaluating in two steps

	"!" Лучше всегда использовать подход с использованием Lock, вместо lock-free, когда не используются локи совсем,
		для повышения оптимизации.

133. Отмена потоков

	"!" Простого и хорошего способа отменять потоки не существует

	Самое простое - убить поток, запустив его в отдельном процессе. 
	Кооперативная отмена = самый адекватный подход
		Чтобы поток А смог отменить поток Б, они должны между собой кооперировать.
		Это реализуется через:
			- булевые флаги
			- флаги на основе примитивов синхронизации
		Unit of Work - паттерн, который упрощает дизайн кооперативной отмены.

134. Отмена убийством процесса

	import multiprocessing

	#start new process
	p = multiprocessing.Process(target=my_func_to_close, args = (variables,))
	p.start()

	#kill process
	p.terminate()

	"!"	Очень опасно, потому что можно повредить данные, так как при закрытии процесса, мы не знаем,
		на каком этапе сейчас функция.

135. Базовая отмена с флагом

	- Самый базовый вариант кооперативной отмены.

	Суть в том, что нужно установить договорённости, что будет происходить в результате отмены.

	#init stop flag
	stop_flag = True

	#check if flag == True
	if stop_flag:
		/actions to prevent data loose etc.

136. Имплементируем отмену через Unit of Work-паттерн

	Unit of Work - это паттерн определяющий логическую транзакцию 
	т.е. атомарную синхронизацию изменений в объектах, помещённых в объект UoW с хранилищем (базой данных).

	Основан на использовании stop_event, и сигналах между событиями в разных блоках кода

	<-->

137. Подытоги

	Преимущества асинхронных операций:
	- надёжность
	- корректность работы
	- ускорение работы
	- работа с большими объёмами данных
	- более плавная работа и мгновенная работа за счёт использования всего ресурса
	- множество современных API написаны в асинхронном стиле

	Сложности:
	- сложный процесс разработки асинхронности и паралелльных вычислений
	- осознание многопоточного кода всегда сложнее последовательного

138. Обработка исключений

	- можно ловить исключения внутри потока
	- можно ловить исключения в вызывающем потоке
	- поток умалчивает об исключениях
	- API потока не даёт возможности отловить в вызывающем потоке
	- ThreadPoolExecutor API даёт возможность отловить исключение в вызывающем потоке

139. Обработка исключений - Демо

	- Для примера, установим команду raise Exception внутри основной вычислительной функции

	"!" Если исключение произошло внутри одного из потоков (не в main-потоке), то main-поток продолжает выполнять операции.
		Поэтому мы и говорим, что поток сам по себе "замалчивает" исключения.

	Решение: ставить обработку исключения внутри основной вычислительной функции. Но верхний уровень не будет знать об
			 исключении, что является проблемой (потому что исключение обрабатывается только на нижнем уровне)

	"!" Вышеописанная проблема решается с помощью ThreadPoolExecutor.

	import concurrent.futures

	#creating thread using API
	with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
		future = executor.submit(func_with_raising_exception, 3, 15)

		#nothing happens until we ask for result from function, inside which we are raising error
		res = future.result()

	#but, now we can handle exception by using try-except block
	try:
		res = future.result()
	except:
		/actions to handle exception

=
-----Раздел 14: Допматериалы-1. Модуль asyncio-----
=

140. Введение в asyncio

	Сердце asyncio - корутины (coroutines)

	Корутины - 	функции, помеченные как async def;
				за кулисами построенные на генераторах
				Возвращают объекты-корутины.

	Программа с корутинами должна в main запустить event loop (цикл обработки событий)

	#call event loop
	acyncio.run()

	Event loop отвечает за запуск корутинов, коллбэков, финализацию асинхронных генераторов и т.д

141. Простейший пример с asyncio

	import asyncio

	#create coroutine function
	async def my_func():

	"!" Чтобы смысл asyncio не потерялся, всё должно быть выставлено асинхронно.

	#async sleep
	await asyncio.sleep(1)

	#gathering function to async - call it asynchrolly
	def main():
		await asyncio.gather(my_func(), my_func(), my_func())

	#start async
	asyncio.run(main())

	- Функция помеченная async == корутин
	- await может быть использован только внутри корутина
	- await обязан быть прописан при вызове корутина
	- yield разрешён в корутинах и создаёт асинхронный генератор
	- return в корутинах разрешён
	- await может быть использован также при вызове любого awaitable-объекта
	- awaitable - объект реализующий __awaitable__(), который возвращает итератор
	- Корутин относится к awaitable-объектам

142. Event Loop. Введение

	#return working event loop or creating it
	asyncio.get_event_loop()

	#return working event loop, but never creates it
	asyncio.get_running_event_loop()

	#starts event loop, work until func() ending
	loop.run_until_complete(func())

	#close event loop
	loop.close()

	#set new courutine to queue
	loop.create_task(new_func())

	#run event loop until stop() command
	loop.run_forever()

	#stop event loop
	loop.stop()

143. Event Loop. Демо

	#check for all created tasks
	asyncio.all_tasks()

	#check if loop is running
	loop.is_running()

	#check if loop is closed 
	loop.is_closed()

144. Демо с aiohttp

	@jsonplaceholder.typicode.com@ - site for training

	#async realisation of photos parsing
	async def photos_by_album(album, session):
		url = f'...siteurl...?albumId={album}'
		response = await session.get(url)
		photos_json = await response.json()
		return [Photo.from_json(photo) for photo in photos_json] 
		#Photo.from_json(photo) it is a class method which constructs new photo using its title, url, etc. from json data

	#using aiohttp in main function
	async def main():
		async with aiohttp.ClientSession() as session:
			photos = await photos_by_album(3, session) #3 == number of album, 
													   #session == current session via aiohttp.ClientSession()

	#run
	asyncio.run(main())

	#another way for def main() - fast unpacking
	async def main():
		async with aiohttp.ClientSession() as session:
			photos = await asyncio.gather(*(photos_by_album(album, session) for i, album in enumerate(range(2, 30))))

145. Демо с aiofiles

	aiofiles - асинхронная работа с файлами

	import aiofiles

	#async reading file
	async def read_large_file():
		async with aiofiles.open(my_path_to_file, 'r') as f:
			return await f.read()

	#async main for reading
	async def main():
		text = await async_read_large_file()

146. Futures & Tasks

	Awaitables - объект который реализует __awaitable__(), который возвращает итератор

	Корутин относится к awaitable

	Task и Future также относятся к awaitable

	Future - специализированный низкоуровневый тип, 
			 представляющий будущий результат выполнения асинхронной функции(корутина)

	Состояния Future:
		- Pending - function scheduled and in the queue
		- Running - set_result(result), set_exception(exception), get_loop()#<-return current Future's loop
		- Done - done(), result(), exception() -> <exception obj>
		- Cancelled - cancelled()

	Task

	- Inherits Future (wrapper)
	- Allow to schedule courutine and then take result when it needs

	#create task from courutine
	loop.create_task() 

	#creates task if given object is courutine, but also can receive Future or Task, just returning them
	loop.ensure_future()

	#done, pending -- runs courutines -> returns results or scheduled courutines
	await asyncio.wait(iterable)

	#results -> returns list of results with the same way as it given in the args row
	await asyncio.gather(iterable)

	#result taker pattern
	#take result as soon as they became completed
	for t in asyncio.as_completed((t1, t2)): #t1, t2 == courutines -> iterable object
		#t == iterable object
		result = await t

	Thread-safety = код потокобезопасен, если работает без ошибок при использовании его из нескольких потоков одновременно
	Большинство asyncio-объектов (такие как Future) - потоконебезопасны.
	В большинстве случаев это не проблема, 
		но если речь идёт о манипуляции состоянием таких объектов из разных потоков, то требуется маршалинг вызова.
	Маршалинг - вызовы Future приходят из одного и того же потока.
	Event loop работает в main thread и запускает задачи и коллбэки в нём же.

	#set callback to schedule from other thread
	loop.call_soon_threadsafe(callback, *args)

	#set courutine to schedule from other thread
	loop.run_courutine_threadsafe(coroutine())

147. Task API - Демо
	###
	async def tick():
		/action
		asyncio.sleep(1)

	async def main():
		t1 = asyncio.create_task(tick())
		t2 = asyncio.ensure_future(tick())

		await t1
		await t2

	asyncio.run(main())

	###
	#other way to run some courutines
	await asyncio.gather(t1, t2)

	###
	#other way to take completed courutines
	for i, t in enumerate(asyncio.as_completed((t1, t2)), start = 1):
		result = await t

	"!" Чем for enumerate отличается от gather()?
			- for enumerate берёт результаты сразу по мере их поступления, 
			  а gather() накапливает все готовые результаты, и только потом их отдаёт

	###
	#simple way to get json with async
	async def get_json(url):
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as response:
				return await response.json()

148. Обёртываем Thread через Future

	#set result to future from other thread
	loop.call_soon_threadsafe(future.set_result, 1)

149. async for

	С помощью for можно проходить циклом по итератору или генератору

	С помощью async for можно проходить циклом по асинхронному генератору

	"!" async for не распараллеливает итерации!
		async for позволяет последовательно итерировать по асинхронному источнику!

	Асинхронный объект-итератор реализует __aiter__ и __anext__

150. Обработка исключений

	Можно ловить исключения внутри потока

	Можно ловить в вызывающем потоке

	Корутина, выбросившая исключение, прекращает работу, но программа продолжает работу. Исключение "проглатывается"

	await и future.result() пробрасывает исключение, и если это в main thread, приложение погибает

	Проброс исключения из callback навешенного на ensure_future() / create_task() не убивает приложение

	gather(return_exceptions = true) 
		- позволяет взять результаты из успешно выполненных задач и получить список исключений из проваленных

151. Обработка исключений - Демо

	<-->

152. Отмена. Введение

	Future определяет cancel()
		- Если задача ещё не была запущена, то запуск будет отменён.
		- пробрасывается CancelledError
		- задача может проверять CancelledError
		- есть возможность делать кооперативную отмену
		- действует только на pending-задачи
		- некооперативная отмена базируется на исключениях

	future = asyncio.gather(*aws, return_exceptions = False)
		- исключение пролетает до await, остальные таски не отменяются
		- если return_exceptions = True, то исключения идут в результаты
		- явный cancel() на pending-тасках отменяет их
		== делать cancel на future -> опасно

	asyncio.wait(*aws, timeout, return_when = ALL_COMPLETED)
		- return_when = FIRST_COMPLETED
		- return_when = FIRST_EXCEPTION
		- Не отменяет таски по истечению таймаута

153. Отмена с gather

	#cancel in other thread
	loop.call_soon_threadsafe(future.cancel)

154. Отмена с wait. Кооперативная отмена

	<-->

155. async IO vs sync IO

	"!" При загрузке сайтов, асинхронный подход при использовании threading работает примерно в 3 раза быстрее.
		А при использовании asyncio, в 10 раз быстрее!

'''
here part about sql language has skipped and moved to file sql-manual.sql in refined model
'''
=
-----Раздел 16: Python & SQL-----
=

215. Введение

	Direct Connectors (Adapters) - позволяет "вручную" работать с SQL.
		- psycopg2
		- mysql.connector
		- cx_Oracle
		- Sqlite3 (built-in)
		- OmniDB

	ORM (Object Relational Mapper - объектно-реляционный преобразователь)
		- SQLAlchemy
		- Storm
		- Django Built-in
		- peewee

216. psycopg2

	import psycopg2

	#set connection to data base
	conn = psycopg2.connect(dbname = 'testdb', user = 'postgres', password = '123456')
	-> Connection object

	#set cursos for work with database
	cur = conn.cursor()
	-> Cursor object

	#set SQL command to queue with cursor
	cur.execute("DROP TABLE IF EXISTS superheroes") #it is not executes simultaneously! just sets as a future operation

	#necessaty way to set parameters - using placeholders
	cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s)", ("Superman", 100))
																		#never use '%' instead of ','!!!
																		#because we setting arguments, not final string!
																		#only use %s!
																#if we set one argument - we write (10,) with end-comma

	#set parameters with dictionary
	cur.execute("""
				INSERT INTO superheroes (hero_name, strength)	
				VALUES (%(name)s, %(strength)s);
				""", {'name': 'Maks The Great', 'strength': 999})

	#perform all cur.execute() commands, setted before
	conn.commit() #better to call it after logic blocks - inserting, altering etc.

	#get one line from cursor queue
	one_line = cur.fetchone()

	#get full data from cursor
	full_fetch = cur.fetchall()
	#we also can iterate it
	for record in full_fetch:
		print(record)

	#close cursor
	cur.close()

	#close connection
	conn.close()

	@Adaptation of Python values to SQL types
	https://www.psycopg.org/docs/usage.html
		
	#massive inserting
	import RealDictCursor
	#
	with psycopg2.connect(dbname = 'testdb', user = 'postgres', password = '123456') as conn:
		with conn.cursor(cursor_factory = RealDictCursor) as curs: #set type of cursor for dict reading
			#send list of tuples as values for table
			execute_values(curs, "INSERT INTO traffic_light (light) VALUES %s", [("green",), ("yellow",), ("red",)])
			#then we can use fetching
			curs.execute("SELECT * FROM traffic_light")
			records = curs.fetchall()
			print(records)
			-> list of type RealDictRow #if cursor_factory = RealDictCursor
			#also we can catch dictionary elements == if cursor_factory = RealDictCursor
			print(records[0]["light"])
			-> "green" #returns first setted element
			#after all action in this block -> all cursors inside closes and connection implementing as commited

217. ORM и SQLAlchemy

	import sqlalchemy

	#creating engine
	engine = sqalchemy.create_alchemy('postgresql+psycopg2://postgres:123456@localhost:5432/testdb')
										#sqlsystem+adapter://username:password@hosttype:host/dbname

	#we can use sqlalchemy as adapter -- setting connection
	connection = engine.connect()
	#supporting same operations as psycopg2
	result = connection.execute("SELECT * FROM book")

	#start transaction
	trans = connection.begin()
	#
	try:
		connection.execute(/SQL ACTION) #execute some SQL code
		trans.commit() #commit this code
	except:
		trans.rollback() #if exception inside, rollback to origin state
		raise

	"!" Чтобы использовать SQLAlchemy по назначению, необходимо описать таблицы из БД специальными классами,
		а затем их декорировать методами SQLAlchemy.

	 #we should use declarative_base for out class inheritance
	 Base = declarative_base()
	 #
	 class Author(Base):
	 	__tablename__ = 'author' #name of table we working with
	 	#we can set parameters by classes of SQLAlchemy
	 	author_id = Column(Integer, primary_key = True)
	 	full_name = Column(String(length = 25))
	 	rating = Column(Float)

	"!" Connection in SQLAlchemy is like a long transaction which stores actions.

	#we can create special metadata to work with using engine	 
	Base.metadata.create_all(engine)
	#
	Session = sessionmaker(bind = engine)
	#
	session = Session()
	#
	author = Author(author_id = 18, full_name = 'Dan Brown', rating = 4.7)
	#
	session.add(author)
	#
	session.commit()
	#we can iterate through ordered or filtered table
	for item in session.query(Author).order_by(Author.rating):
		print(item.full_name, ' ', item.rating)

-----------------------------------------------------------------------------------------------------------------------------







