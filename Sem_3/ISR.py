#Задание 1.2

import math
def f(a1,a,n):
  sum = (a1+a)*n/2
  return sum
print(f(1,5,5))

#Задание 1.3

def geron(p,a,b,c):
  sum = math.sqrt(p*(p-a)*(p-b)*(p-c))
  return sum
print(geron(11,4,4,10))

#Задание 1.4

print("Vvedite pervoe chislo")
a=float(input())
print("Vvedite vtoroe chislo")
b=float(input())
print("Vvedite operaciyu: +,-,*,/")
c=str(input())

def f(a,b,c):
  if c=="+":
   print(a+b)
  if c=="-":
   print(a-b)
  if c=="*":
   print(a*b)
  if c=="/":
    if b==0:
     print("Delenie na 0!")
    else:
     print(float(a/b))
f(a,b,c)

#Ссылки на repl
#https://repl.it/@ulyaakwatore/Tema-1-ISR-12-13#main.py
#https://repl.it/@ulyaakwatore/Tema-1-ISR-14#main.py
