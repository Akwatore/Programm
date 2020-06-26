#Задание 3.1(2)

from random import randint
 
attempts = 1
Var1 = randint(1,100)
print ("Загадано число от 1 до 99")
Var2 = int(input("Ваш вариант? - "))
while Var1 != Var2:
    if Var1 > Var2: print ("Угадываемое число больше {0} ".format(Var2))
    elif Var1 < Var2: print ("Угадываемое число меньше {0} ".format(Var2))
    attempts += 1
    Var2 = int(input("Ваш вариант? - "))
print ("Вы угадали число {0} за {1} попыток ".format(Var2, attempts))


#Задание 3.2(1)

for i in range(65, 91):
  print(chr(i), end='')
for i in range(97, 123):
  print(chr(i), end='')
for i in range(1040, 1104):
  print(chr(i), end='')
  
  
  
#Ссылки на repl
#https://repl.it/@ulyaakwatore/Tema-3-VSR-312#main.py
#https://repl.it/@ulyaakwatore/Tema-3-VSR-321#main.py
