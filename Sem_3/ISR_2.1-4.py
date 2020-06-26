#Задание 2.1 и 2.2

#Выполнила: Пляскина Ульяна, ИВТ, 3, 1
#Вариант: 6
#Задание 2, 6, 13

#Постройте таблицу истинности для: 
#2. Стрелка Пирса.
#6. ((C∨B)→B)∧(A∧ B)→B
#13. A∧¬B↔A∨B

def func1(a,b):
  return int(not a and not b)

def f1():
  print('_'*21)
  print(chr(124)+'  A'+'  '+chr(124)+' '+' B  '+chr(124)+' '+'A ↓ B '+''+chr(124))
  print('-'*21)
  for a1 in range(0,2):
    for b1 in range(0,2):
      print('| ', a1,' | ', b1 , ' |  ',func1(a1,b1), '  |');
      print('-'*21) 

f1()

def func2(a,b,c):
  return int(1)

def f2():
  print('_'*40)
  print(chr(124)+'  A'+'  '+chr(124)+' '+' B  '+chr(124)+' '+' C  '+chr(124)+' ((C∨B)→B)∧(A∧ B)→B '+''+chr(124))
  print('-'*40)
  for a1 in range(0,2):
    for b1 in range(0,2):
      for c1 in range(0,2):
        print('| ', a1,' | ', b1 , ' | ', c1, ' |         ' ,func2(a1,b1,c1), '        |');
        print('-'*40) 

f2()

def func3(a,b):
  return int((not a and not b) or (a and not b))

def f3():
  print('_'*25)
  print(chr(124)+'  A'+'  '+chr(124)+' '+' B  '+chr(124)+' '+' A∧¬B↔A∨B '+''+chr(124))
  print('-'*25)
  for a1 in range(0,2):
    for b1 in range(0,2):
      print('| ', a1,' | ', b1 , ' |    ',func3(a1,b1), '    |');
      print('-'*25) 

f3()



print('-'*41)
print(chr(124) + '  A'+'  '+chr(124)+'  B'+'  '+ chr(124)+ '  '+'A ∧ B  ' + chr(124)+'  '+ 'A ∨ B'+'  '+ chr(124)+ '  '+'A→B  '+chr(124))
print('-'*41)
a = False
b = False
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '    '+str(int(a and b))+ '    ' + chr(124)+'    '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '   '+chr(124))
print('-'*41)
a = False
b = True
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '    '+str(int(a and b))+ '    ' + chr(124)+'    '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '   '+chr(124))
print('-'*41)
a = True
b = False
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '    '+str(int(a and b))+ '    ' + chr(124)+'    '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '   '+chr(124))
print('-'*41)
a = True
b = True
print(chr(124)+ '  ' + str(int(a))+ '  '+chr(124)+'  '+ str(int(b))+'  '+ chr(124)+ '    '+str(int(a and b))+ '    ' + chr(124)+'    '+ str(int(a or b))+'    '+ chr(124)+ '   '+str(int(not a or b))+ '   '+chr(124))
print('-'*41)



#Задание 2.3

#Выполнила: Пляскина Ульяна, ИВТ, 3, 1
#Вариант: 6(5)
#Задание 6, 20(24)

# Описание задачи
 # Дан список: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
 # Для данного списка, используя слайсы, обращение к элементам по 
 # индексу, методы sum(), min(), max(), арифметические операторы (не используя циклы или условные операторы) найдите:

# 6. Минимальный элемент, стоящий на нечетной позиции среди элементов первой половины списка. 
# (Сделано в 2018 году - https://repl.it/@ulyaakwatore/20-09-18)

lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

lst1 = lst[1:len(lst):2]
print(min(lst1))

# 24. Список, в котором бы содержались размеры автомобиля (длина, ширина, высота)
# (Сделано в 2018 году - https://repl.it/@ulyaakwatore/Template-for-assignment-1)
  # Дан кортеж:
car = ('name', 'DeLorean DMC-12', 'motor_pos: rear', 'n_of_wheels', 4, 'n_of_passengers', 2, 'weight', 1.230, 'height', 1.140, 'length', 4.216, 'width', 1.857, 'max_speed', 177) 

lst1 = car[9:15]
print(lst1)


#Задание 2.4

#Выполнила: Пляскина Ульяна, ИВТ, 3, 1

# Постановка задачи: ящик, имеющий форму куба с ребром a см без одной грани, нужно покрасить со всех сторон снаружи. Найдите площадь поверхности, которую необходимо покрасить. Ответ дайте в квадратных сантиметрах.

def sqare(a):
  s=a*a*5
  print('Площадь поверхности, которую необходимо покрасить =', '%.3f' % s, 'см^2')

a=float(input())

if a>0:
  sqare(a)
else:
  print('Введите значение больше 0')
  
  

#Ссылки на repl
#https://repl.it/@ulyaakwatore/Tema-2-ISR-21-22#main.py
#https://repl.it/@ulyaakwatore/Tema-2-ISR-23#main.py
#https://repl.it/@ulyaakwatore/Tema-2-ISR-24#main.py
