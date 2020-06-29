from random import randint

def sort(nums):  
    for i in range(1, len(nums)):
        k = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > k:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = k


z = []
for i in range(10):
    z.append(randint(-10, 10))
sort(z)
print('метод вставки')  
print(z)  

print('встроенные функции')
print(sorted(z))


print('распределение списка с случайными значениями на два списка по определенному критерию')
a = []
b = []

for i in z:
    if i < 0:
        a.append(i)
    else:
        b.append(i)

print(a)
print(b)
