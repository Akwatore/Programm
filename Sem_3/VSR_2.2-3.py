#Задание 2.2

def f(base_seq):
  res = []
  for item in base_seq:
    if item in res:
      continue
    else:
      res.append(item)
  return res
lst = [1,2,2,3,3,3,4,5,5,6]
print(f(lst))


#Задание 2.3

l1 = [1,2,3]
l2 = [4,5,6]

print(list(zip(l1,l2)))
print (list(map(lambda x,y: (x, y), l1, l2)))


#Ссылка на repl
#https://repl.it/@ulyaakwatore/Tema-2-VSR-22#main.py
#https://repl.it/@ulyaakwatore/Tema-2-VSR-23#main.py
