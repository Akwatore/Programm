#Задание 3.1

import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from urllib.request import urlopen
from xml.etree import ElementTree as ET


def get_currencies(currencies_ids_lst=['R01239', 'R01235', 'R01035']):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')

        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            result[valute_id] = valute_cur_val

    return result


# TODO 0

# Вывести на графике 10 валют (получить по кодам валюты из ЦБС)

cur_vals = get_currencies()

objects = cur_vals.keys()

print(cur_vals)
y_pos = np.arange(len(objects))

# TODO #1 переписать лямбда-функцию из следующей строки через list comprehension

# или генераторы списков (как мы их называем)
performance = list(
    map(lambda x: float(x.replace(",", ".")), cur_vals.values()))

# TODO #2

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков),
# столбцы должны быть разных цветов с легендой

# TODO #3

# Нарисовать отдельный график с колебанием одной (выбранной вами) валюты
# (получить данные с сайта ЦБ за год) и отобразить его наиболее
# оптимальным образом (типом графика)

# TODO #4

# Отобразить это на одном изображении (2 графика)

plt.bar(y_pos, performance)
# plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()


#Задание 3.2

def poisk():
  str = input("Vvedite stroku ")
  pstr = input("Vvedite podstroku ")
  print(str.find(pstr))

poisk()


#Задание 3.4

import codecs
print(codecs.encode(input("Vvedite stroku: "), "rot_13"))



#Ссылки на repl
#https://repl.it/@ulyaakwatore/Tema-3-ISR-31#main.py
#https://repl.it/@ulyaakwatore/Tema-3-ISR-32#main.py
#https://repl.it/@ulyaakwatore/Tema-3-ISR-34#main.py
