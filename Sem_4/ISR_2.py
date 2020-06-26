def logger(function):
    import functools
    @functools.wraps(function)
    def wrapper(*args):
       
        if function.__name__ == 'add':
            operation_name = "Сложение"
        elif function.__name__ == 'diff':
            operation_name = "Вычитание"
        elif function.__name__ == 'mult':
            operation_name = "Умножение"
        elif function.__name__ == 'divis':
            operation_name = "Деление"
        else:
            operation_name = "Неизвестная операция"
    
        result = function(*args)

        with open('Record.txt', 'a') as f:
            f.write("\n")
            f.write("Функция: " + operation_name + "\n")
            f.write("Аргументы: " + str(args) + "\n")
            f.write("Результат: " + str(result) + "\n")
            f.write("\n")
            f.write("\n")
        return result
        
    return wrapper


@logger
def add(*args):
    res = 0
    for arg in args:
        res += arg
    return res

@logger
def diff(*args):
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res -= arg
    return res

@logger
def mult(*args):
    res = 1
    for arg in args:
        res *= arg
    return res

@logger
def divis(*args):
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res /= arg
    return res


@logger
def calc():

    choice = input(' Введите номер действия: \n 1.Сложение, 2.Вычитание, 3.Умножение, 4.Деление \n')

    if choice == '1':
        print('Введите слагаемые через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = add(*arr)
        print("Ответ:", result)
    elif choice == '2':
        print('Введите уменьшаемое и вычитаемые через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = diff(*arr)
        print("Ответ:", result)
    elif choice == '3':
        print('Введите множители через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = mult(*arr)
        print("Ответ:", result)
    elif choice == '4':
        print('Введите делимое и делители через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = divis(*arr)
        print("Ответ:", result)
    else:
        print('Некорректный ввод')
calc()
