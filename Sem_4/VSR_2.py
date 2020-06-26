from datetime import datetime, date, time

def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def number():
    l = []
    for i in range (10000):
        l.append(i)
    return l

print(number())
