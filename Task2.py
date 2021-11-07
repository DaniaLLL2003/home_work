'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('workers.txt', 'r', encoding="utf-8") as file:
    dict = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f'Average salary = {round(sum(dict.values()) / len(dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in dict.items() if e[1] < 20000]}')