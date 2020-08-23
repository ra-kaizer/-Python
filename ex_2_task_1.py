# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

# https://drive.google.com/file/d/1BTNJvHu3bJ7Omb7EPpp6p6F-lrb3O_MS/view?usp=sharing

# начало
# Ввод сообщения "stop" для выхода из цикла
# Запустить бесконечный цикл # (ромб)
    # Запросить ввод знака операции ("Что делаем? (+,-,*,/): ")
    # Если был введен "stop", то прервать цикл операцией
    # Запросить первое число
    # Запросить второе число
    # Ввести арифмет.действие в зависимости от знака:
    # если +, первое число + второе число
        # вывести результат
    # если -, первое число - второе число
        # вывести результат
    # если *, первое число * второе число
        # вывести результат
    # если /, первое число / второе число
        # вывести результат, округлить до 2 знаков
    # Иначе, Ошибка при делении на ноль, вывести сообщение "на ноль делить нельзя, даже если очень хочется"
# Иначе "Вы ввели неверную операцию!"
# Конец


print("Введите \"stop\" для выхода!")
while True:
    question = input("Что делаем? (+,-,*,/): ")
    if question == 'stop':
        break
    if question in ('+', '-', '*', '/'):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if question == "+":
            res = a + b
            print(f"Результат: {res}")
        elif question == "-":
            res = a - b
            print(f"Результат: {res}")
        elif question == "*":
            res = a * b
            print(f"Результат: {res}")
        elif question == "/":
            if b != 0:
                res = a / b
                res = round(res, 2)
                print(f"Результат: {res}")
            else:
                print("На ноль делить нельзя, даже если очень хочется! Попробуйте еще раз!")
else:
    print("Вы ввели неверную операцию!")
