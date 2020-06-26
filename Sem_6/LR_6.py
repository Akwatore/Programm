# Программирование (Python)
# 6 семестр, тема 2

# Лабораторная работа 6

"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""

def get_fib_nums_lst(n: int) -> list:
    if n == 0:
        return 'неверный аргумент n'
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_lst = get_fib_nums_lst(n-1)
    fib_lst.append(fib_lst[-1] + fib_lst[-2])
    return fib_lst

print(get_fib_nums_lst(0))
print(get_fib_nums_lst(1))
print(get_fib_nums_lst(2))
print(get_fib_nums_lst(5))
print(get_fib_nums_lst(10))


#Ссылка на repl
#https://repl.it/@ulyaakwatore/Sem-6-Lr-6#main.py
