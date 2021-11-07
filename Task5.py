'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

def rewrite_file():
    try:
        with open('sum.txt', 'r+') as file:
            file.write(input('Введите числа через пробел: '))
            l = map(int, file.read().split())
            print(sum(l))
    except FileNotFoundError:
        return 'Файл не найден.'

