#Создание программы, возвращающей список чисел Фибоначчи с помощью генератора.

def fib(k):
  fib_sum, fib1, fib2 = 0, 0, 1
  while fib_sum < k:
    fib_sum = (fib1 + fib2)
    fib1 = fib2
    fib2 = fib_sum
    if fib_sum > k:
      break
    yield fib_sum


f = ([0,1]+list(fib(int(input("Введите число: ")))))
print(f)
