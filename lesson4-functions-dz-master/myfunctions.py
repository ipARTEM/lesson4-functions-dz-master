# Функция создает красивый резделитель из 10-и звездочек (**********)
def simple_separator():
    print('*' * 10)


simple_separator()

# print(simple_separator() == '**********')  # True

"""
 Функция создает разделитель из звездочек число которых можно регулировать параметром count
 :param count: количество звездочек
 :return: строка разделитель, примеры использования ниже
 """


def long_separator(count):
    print('*' * count)


long_separator(3)
long_separator(4)

"""
  Функция создает разделитель из любых символов любого количества
  :param simbol: символ разделителя
  :param count: количество повторений
  :return: строка разделитель примеры использования ниже
  """


def separator(simbol, count):
    print(simbol * count)


separator('-', 10)
separator('#', 5)

"""
Функция печатает Hello World в формате:
**********

Hello World!

##########
:return: None
"""


def hello_world():
    separator('*', 10)
    print('')
    print('Hello World!')
    print('')
    separator('#', 10)


'''
**********

Hello World!

##########
'''
hello_world()

"""
Функция печатает приветствие в красивом формате
**********

Hello {who}!

##########
:param who: кого мы приветствуем, по умолчанию World
:return: None
"""


def hello_who(who='World'):
    print(f'Hello {who}!')


'''
**********

Hello World!

##########
'''
hello_who(who='World')
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')

"""
 Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
 :param power: степень
 :param args: любое количество цифр
 :return: результат вычисления # True -> (1 + 2)**1
"""


def pow_many(power, *args):
    result = 0
    for number in args:
        result += number
    return result ** power


print(pow_many(1, 1, 2))  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3))  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1))  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2))  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4))  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

"""
Функция выводит переданные параметры в фиде key --> value
key - имя параметра
value - значение параметра
:param kwargs: любое количество именованных параметров
:return: None
"""


def print_key_val(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f' {k} --> {v}')


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)

"""
(Усложненное задание со *)
Функция фильтрует последовательность iterable и возвращает новую
Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
(примеры ниже)
:param iterable: входная последовательности
:param function: функция фильтрации
:return: новая отфильтрованная последовательность
"""


def my_filter(iterable, function):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    return result


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))  # True == [4, 5]
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))  # True == [2]
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))  # True == [1, 2, 4, 5]
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))  # True == ['a', 'b']
