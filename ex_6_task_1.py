"""
ex_6_task_1
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
# 32-х разрядная версия интерпретатора Python /Python 3.8.2 [MSC v.1916 32 bit (Intel)] on win32
# 64-разрядная версия ОС Windows 10
"""
ex_2_task_9. 
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму 
его цифр.

Примечание:
здесь представлено 3 варианта задач, каждая разобрана в отдельном файле (test_1, 2, 3) с помощью модуля sys.getsizeof
"""
# 1 вариант
n = int(input("Введите число с новой строки, по окончании введите 'Ноль' и нажмите Enter\n"))
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input())
print(f'максимальное число {max_m} имеет сумму цифр: {max_s}')
# удалим временные значения
del s, m, n

# 2 вариант
def sum_numbers(num):
    sum_ = 0
    for f in num:
        sum_ += int(f)
    return sum_


list_number = [i for i in input('Введите числа через пробел и нажмите Enter: ').split()]

max_n = 0
max_s = 0
for i in list_number:
    if sum_numbers(i) > max_s:
        max_n = i
        max_s = sum_numbers(i)

print(f'максимальное число {max_n} имеет сумму цифр: {max_s}')
del list_number, i

# 3 вариант
list_number = [int(x) for x in input("Введите последовательность натуральных чисел: ").split()]
max_num = max(map(int, list_number))


def sum_digits(num):
    return num % 10 + sum_digits(num // 10) if num > 9 else num


print(f'максимальное число {max_num} имеет сумму цифр: {sum_digits(max_num)}')
del list_number

# _________________________________________________________________________
""" Вывод:
№1 переменные занимают 28 байт

№2 переменные при удалении списка list_number занимают 41 байт, сам список list_number занимает 44 байт содержащий 
ссылки на объекты, также объекты внутри списка list_number занимают место. Итого суммарно 190 байт
Так как лучше неиспользуемый объект удалить, то мы удалим список list_number.
Итого перемеенные занимают 41 байт.

№3
Список list_number занимает 44 байта + объекты внутри списка каждый занимают место. Итого 112 байт.
При удалении list_number, т.к это врененная переменная освобождается место. удаляем list_number
Итого 14 байт.

общий вывод: какой из трёх вариантов лучше и почему.
оптимальным вариантом являет вариант №3 в 14 байт, занимает наименьшее количество помяти, при условии удаления
временных переменных
"""
