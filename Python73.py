'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),которая принимает в качестве аргумента функцию, вычисляющую 
элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.'''

def print_table(operation, num_rows, num_columns, op):
    
    if op == 0:
        n = 0
    if op == 1:
        n = 1
    if op == 2:
        n = 1

    for i in range(n, num_rows + 1):                                        #Формирование таблиц
        answer = []
        for j in range(n, num_columns + 1):
            answer.append(str(operation(i, j)))
            
        if (i ==1) and (op == 2):                                           #Условие для формирования таблицы степеней
            print('    \t'.join([i for i in answer1[:num_columns]]))
        else: 
            print('    \t'.join(answer))

num_rows = int(input('Введите количество строк таблицы: '))                 #Приглашение ко вводу количества строк
num_columns = int(input('Введите количество столбцв таблицы: '))            #Приглашение ко вводу количества столбцов

answer1 = []
for j in range(num_columns):                                                #Формирование списка (будет строкой 0) для таблицы степеней
    answer1.append(str(j+1))


print('---------Таблица сумм----------------')                              #Вывод таблиц
print_table(lambda x, y: x + y, num_rows, num_columns, op=0)
print('--------------------------------')
print('---------Таблица умножения-----------')
print_table(lambda x, y: x * y, num_rows, num_columns, op=1)
print('--------------------------------')
print('---------Таблица степеней-------------')                              
print_table(lambda x, y: x**y, num_rows, num_columns, op=2)