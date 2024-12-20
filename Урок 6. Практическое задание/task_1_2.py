"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
Задание взял из Урок 5, task_1.
"""

"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from memory_profiler import memory_usage
from timeit import timeit

num_of_companies = 10000
dictionary = {f"Рога {i}": i for i in range(num_of_companies)}
"""
Закомментировал, чтобы на тестах не осуществлять ввод с клавиатуры
и предварительно создаю словарь для тестирования времени, используемой памяти. 
# Ввод количества предприятий
num_of_companies = int(input("Введите количество предприятий для расчета прибыли: "))

for i in range(num_of_companies):
    # Ввод названия предприятия
    company_name = input("Введите название предприятия: ")
    # Ввод прибыли предприятия за каждый квартал
    quarters_profit = input(f"через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
    # Сохранение прибыли в словарь
    dictionary[company_name] = sum(map(int, quarters_profit.split()))
"""


# Создаем функцию-обертку, которая будет измерять и выводить использование памяти.
def count_memory_usage(func):
    def wrapper(*args, **kwargs):
        mem_before = memory_usage()[0]
        print(f'Время выполнения: {timeit(lambda: func(*args, **kwargs), number=1000)} секунд')
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию с параметрами
        print(f'Использовано памяти: {memory_usage()[0] - mem_before} MiB')
        return result

    return wrapper


# Оборачиваем цикл из решенного задания в функцию и декорируем для измерения
# потребляемой памяти и времени выполнения.
@count_memory_usage
def divide_by_average_revenue():
    # Получение и вывод в консоль средней годовой прибыли.
    average_companies = sum(dictionary.values()) / num_of_companies
    # print(f"Средняя годовая прибыль всех предприятий: {average_companies}")

    # Поиск и вывод в консоль предприятий с прибылью выше среднего.
    find_above_average = [name for name, profit in dictionary.items() if profit > average_companies]
    find_above_average = f"Предприятия, с прибылью выше среднего значения: {', '.join(find_above_average)}"

    # Поиск и вывод в консоль предприятий с прибылью ниже среднего.
    find_below_average = [name for name, profit in dictionary.items() if profit < average_companies]
    find_below_average = f"Предприятия, с прибылью ниже среднего значения: {', '.join(find_below_average)}"
    return find_above_average, find_below_average


# Оптимизированная версия с предварительно созданными списками и
# с использованием одного цикла для обхода.
@count_memory_usage
def divide_by_average_revenue_optimized():
    # Получение средней годовой прибыли
    average_companies = sum(dictionary.values()) / num_of_companies
    # Списки для хранения данных о предприятиях с прибылью выше и ниже среднего.
    above_average, below_average = [], []
    # Перебор в цикле и распределение предприятий по спискам.
    for name, profit in dictionary.items():
        if profit > average_companies:
            above_average.append(name)
        else:
            below_average.append(name)
    above_average = f"Предприятия, с прибылью выше среднего значения: {', '.join(above_average)}"
    below_average = f"Предприятия, с прибылью ниже среднего значения: {', '.join(below_average)}"
    return above_average, below_average


# Запуск исходной версии.
divide_by_average_revenue()
# Запуск оптимизированной версии с использованием filter.
divide_by_average_revenue_optimized()

"""
Можно заметить, что использование двух списков для хранения названий предприятий
с прибылью выше и ниже среднего уменьшило и время и потребляемую память,
поскольку итерация была выполнена 1 раз.
Время выполнения: 2.038708799998858 секунд
Использовано памяти: 0.21484375 MiB
Время выполнения: 1.6103848999991897 секунд
Использовано памяти: 0.10546875 MiB
"""
