"""
Вне класса прописаны вспомогательные функции
"""

# heyheygogoleva privet s githaba

import random
import string
import pandas as pd





def generate_random_string(length):
    """
    Функция для генрации строк

    Позволяет сгенерирвоать строку указанной дллины, заполненную случайными символами.

    Аргументы: legnth (int) - длина строки, которую необходмио сгенерировать.

    Возвращает: строковую переменную random_str (str)

    """
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def make_table(n):
    """
    Функция для создания таблиц

    Позволяет создать csv-таблицу с данными, соответсующими варианту, в той же директории, где находится  файл с кодом. 

    Аргументы: n (int) - размер таблицы (количество строк)

    Возвращает: возвращаемые значения отсутсвуют. 

    """
    full_names = []
    ranks = []
    numbers = []
    ages = []
    for i in range(n):
        name_lenghth = random.randint(10, 25)
        rank_length = random.randint(8, 16)
        full_names.append(generate_random_string(name_lenghth))
        ranks.append(generate_random_string(rank_length))
        numbers.append(random.randint(1, 20))
        ages.append(random.randint(20, 65))
    table_name = '/Users/sofia/Desktop/учеба/3 курс/методы проги/лаба2/table' + str(n) + '.csv'
    df = pd.DataFrame({'ФИО': full_names, 'звание': ranks, 'номер роты': numbers, 'возраст': ages})
    df.to_csv(table_name, index= False)
    print(table_name)

ns = [100, 500, 1000, 5000, 10000, 50000, 100000, 200000]
for i in ns:
    make_table(i)


def read_table(n):
    """
    Функция для считывания таблиц

    Позволяет считываеть из той же директории, в которой находится код, csv-таблицы в pandas.DataFrame-таблицы для дальнейшей работы с ними.

    Аргументы: список из размерностей (кол-во строк) таблиц n (list[int])

    Возвращает: список из таблиц tables (list[pandas.DataFrame])
    """
    tables = []
    for i in n:
        table_name = 'table' + str(i) + '.csv'
        table_from = pd.read_csv(table_name)
        tables.append(table_from)
    return tables

tables = read_table(ns)

class Table:
    """
    Класс, объектом которого являются "строчки таблицы" в соотвествии с вариантом. 
 
    Хранит в себе информацию о служащих воинского полка: ФИО, звание, номер роты, возраст. 
    """

    


    def __init__(self, raw: pd.core.series.Series):
        """Конструктор.

        Заполняет поля класса соответсвующими значениями (каждая ячейка таблицы в соответсвтии со стобцом дает поле класса).

        Аргументы: self, строчка таблицы pandas.DataFrame  - raw (pd.core.series.Series)
 
        Возвращает: возвращаемое значение отсутсвует.
        """

    

        self.name = raw[0] 
        ## @var name
        #  ФИО служащего (str)
        self.status = raw[1]
        ## @var status
        #  звание служащего (str)
        self.number = raw[2]
        ## @var number
        #  номер роты служащего (int)
        self.age = raw[3]
        ## @var age
        #  возраст служащего (int)

       

   
    def __eq__(self, other): #x = y
        """
        Оператор сравнения.

        Проверяет, являются ли равными два объекта класса, сопоставляя все поля объектов друг с другом.

        Аргументы: self и other.
 
        Возвращает: bool (True - если объекты равны, False - в ином случае).
        """ 
        if self.name == other.name:
            if self.status == other.status:
                if self.number == other.number:
                    if self.age == other.age:
                        return True
        return False
    



    def __ne__(self, other): #x != y
        """Оператор сравнения.

        Проверяет, являются ли не равными два объекта класса.

        Аргументы: self и other.
 
        Возвращает: bool (True - если объекты не равны, False - в ином случае).
        """
 
        if self == other:
            return False
        else:
            return True


    
    def __lt__(self, other): #x < y
        """
        Оператор сравнения.

        Проверяет, являются ли один объект класса меньше другого, сравнивая поля в соотвествующем порядке (звание,  ФИО, номер роты).

        Аргументы: self и other.
 
        Возвращает: bool (True - если первый переданный аргумент меньше второго, False - в ином случае).
        """ 
        if self.status < other.status:
            return True
        elif self.status == other.status:
            if self.name < other.name:
                return True
            elif self.name == other.name:
                if self.number < other.number:
                    return True
        return False
    

 
    def __gt__(self, other): #x > y
        """
        Оператор сравнения.

        Проверяет, являются ли один объект класса больше другого, сравнивая поля в соотвествующем порядке (звание,  ФИО, номер роты).

        Аргументы: self и other.
 
        Возвращает: bool (True - если первый переданный аргумент больше второго, False - в ином случае).
        """ 

        if self.status > other.status:
            return True
        elif self.status == other.status:
            if self.name > other.name:
                return True
            elif self.name == other.name:
                if self.number > other.number:
                    return True
        return False
    


    def __le__(self, other): #x <= y
        """
        Оператор сравнения.

        Проверяет, два объекта класса на нестрогое неравенство - меньше или равно.

        Аргументы: self и other.
 
        Возвращает: bool (True - если первый переданный аргумент меньше или равен второму, False - в ином случае).
        """ 
        if (self < other) or (self == other):
            return True
        else:
            return False
        
    def __ge__(self, other): #x >= y
        """
        Оператор сравнения.

        Проверяет, два объекта класса на нестрогое неравенство - больше или равно.

        Аргументы: self и other.
 
        Возвращает: bool (True - если первый переданный аргумент больше или равен второму, False - в ином случае).
        """ 
        if (self > other) or (self == other):
            return True
        else:
            return False


def table_to_class(pds):
    """
    Функция для создания объектов класса Table из табличных данных.
    
    Позволяет преобразовать каждую таблицу в список из объектов класса Table (каждая ячейка таблицы в соответсвии со столбцом становится соответсвующим атрибутом). 

    Аргументы: список из таблиц pds (list[pandas.DataFrame])

    Возвращает: двумерный массив (список из списков, состоящих из объектов класса Table), objects (list[list[Table]])
    
    """
    objects = []
    for pd in pds:
        x = []
        for i in range(len(pd)):
            ob = Table(pd.iloc[i])
            x.append(ob)
        objects.append(x)
    return objects


for_sort = table_to_class(tables)


# пирамидальная сортировка
sys.setrecursionlimit(1000000)
def change_pose(x, i, n): # сравнимает iый элемент с его дочерними 
    """
    Вспомогательная функция для пирамидальной сортировки (является еще и вспомогательной для фуцнкции make_tree).

    Позволяет расположить элементы списка (или его части) определенным образом для построения дерева (расставляет узлы дерева)

    Аргументы: список x (list[Table]), счётчики i (int) и n (int)

    Возвращает: возвращаемые значения отсутствуют. 
    """
    # n - первые n элементов, которые нужны учитывать
    i_left = 2 * i + 1 # левый дочерний узел
    i_right = 2* i + 2 # правый дочерний узел
    i_maxi = i
    if i_left <= n and x[i_left] > x[i_maxi]: # !! <=n - входит в нужный нам диапазон
        i_maxi = i_left
    if i_right <= n and x[i_right] > x[i_maxi]: # !! <=n - входит в первые n  элементов списка
        i_maxi = i_right
        
    if i_maxi == i: # поменялось ли значение
        return
    else:
        x[i_maxi], x[i] = x[i], x[i_maxi] # меняем с одним из дочерних (макс) узлов
        change_pose(x, i_maxi, n) # продолжаем процедуру для нового положения узла - для нового списка
        
def make_tree(x):
    """
    Вспомогательная функция для пирамидальной сортировки

    Позволяет создать дерево (вспомогательная конструкция из отстортированного определенным образом списка (или его части) для пирамидальной сортировки)

    Аргументы: список x (list[Table])

    Возвращает: возвращаемые значения отсутствуют. 
    """
    middle = len(x) // 2
    for i in reversed(range(0, middle+1)):
        change_pose(x, i, len(x)-1)

def pyramid_sort(arr):
    """
    Функция для пирамидальной сортировки (в данном случае пирамидальную сортировку используем как самую быструю сортировку из предыдущей лабораторной работы)

    Позволяет отсортрировать список из объектов класса Table, а также вычислить время, за которое был отсторирован  список.

    Аргументы: список для сортировки arr (list[Table])

    Возвращает: отстортированный список x (list[Table]), время, за которое выполнилась сортировка period (float)
    """
    x = arr.copy()
    start = time()
    make_tree(x) # строим пирамиду / дерево
    for i in reversed(range(0, len(x))): # идем с конца в начало
        x[0], x[i] = x[i], x[0]
        change_pose(x, 0, i-1)
    end = time()
    period = end - start
    return x, period


def line_search(lst, size, key):
    """
    Прямой поиск

    Функция, осуществяющая прямой поиск по списку элементов типа Table, ключ сравнивается с полем status класса Table.

    Аргументы: список lst (list[Table]), размер списка size (int), ключ - значение, которое необходимо найти в списке key (str).

    Возвращает: возвращаемые значения отсутствуют (в соответсвии с заданиями лабораторной работы, каждый вид поиска может ничего не возвращать, так как нас интересует только время, за которое ключ будет обнаружен). 
    """
    for i in lst_f:
        if i.status == key:
            return


def bin_search(lst, start, end, key):
    """
    Бинарный боиск

    Функция, осуществяющая бинарный поиск по списку элементов типа Table, ключ сравнивается с полем status класса Table.

    Аргументы: список lst (list[Table]), начало диапазона для поиска по ключу start (int), конец диапазона для поиска по ключу end (int), ключ - значение, которое необходимо найти в списке key (str).

    Возвращает: возвращаемые значения отсутствуют (в соответсвии с заданиями лабораторной работы, каждый вид поиска может ничего не возвращать, так как нас интересует только время, за которое ключ будет обнаружен). 
    """
    mid = 0
    while (1):
        mid = (start + end) // 2
        if key < lst_f[mid].status:
            end = mid - 1
        elif key > lst_f[mid].status:
            start = mid + 1
        else:
            return


from collections import defaultdict

def make_dict(lst):
    """
    Создание ассоциативного массива

    Функция, осуществяющая создание и заполнение ассоциативного массива (на языке программирования python данному типу контейнера соответсвует defaultdict) на основе передаваемого списка.

    Аргументы: список lst (list[Table]).

    Возвращает: заполненный нужными (взятыми из списка) значениями ассоциативный масств mas_dict (defaultdict)
    """
    mas_dict = defaultdict(list)
    for i in lst_f:
        mas_dict[i.status].append(i)
    return mas_dict
















