#Задание 4.1

print('Библиотеки для тестирования')

print('''\n  unittest - был встроен в стандартную библиотеку Python начиная с версии 2.1. 
Cодержит как тестовую среду, так и test runner. У unittest есть некоторые важные требования для написания и выполнения тестов.''')

print('''\n  nose - Вы можете обнаружить, что когда вы напишете сотни или даже тысячи тестов для своего приложения, 
будет становится все труднее понять и использовать результаты unittest. nose совместим с любыми тестами, 
написанными с использованием среды unittest, и может использоваться в качестве его замены. 
Развитие nose как приложения с открытым исходным кодом отстало, и был создан форк под названием nose2. 
Если вы начинаете изучать тестирование с нуля, рекомендуется использовать nose2 вместо nose.''')

print('''\n  pytest - так же поддерживает созданные тесты с unittest. 
Настоящее преимущество pytest заключается в написании test case. Test case в pytest представляют собой серию функций в файле Python, 
начинающихся с имени test_''')


#Задание 4.2

def factorial(n):
    res = None
    try:
        if type(n) is not int:
            raise TypeError('Вы ввели другой тип')
        n =int(n)
    except(ValueError, TypeError):
        print('Входной аргумент не являтся целым натуральным числом')
    else:
        if n<0:
            print('Вы ввели отрицательное число')
        elif n==0:
            return 1
        else:
            res = n * factorial(n-1)
            return res

print('1. ', factorial(3))
print('2. ', factorial(0))
print('3. ', factorial(-2))
print('4. ', factorial(3.14))
print('5. ', factorial('g'))

print('\nТесты\n')

assert factorial(3) == 6
assert factorial(0) == 1
assert factorial(-234) == None
assert factorial(0.34) == None
assert factorial('j') == None
