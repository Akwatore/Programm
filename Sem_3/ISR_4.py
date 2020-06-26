try:
    import json
    import pandas
    import pandas as pd
except:
    print("Ошибка при попытке импартировать модуль")

try:
    with open('ИСР.json', 'r') as read_file:
        data = pandas.read_json('ИСР.json')
        dfdt = pd.DataFrame(data)
        print(dfdt)
except json.JSONDecodeError:
    print("не json")
