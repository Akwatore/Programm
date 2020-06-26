def my_print(line = []):
    lenCol = 30
    for i in range(len(line[0])):
        newArray = []
        for i2 in range(len(line)):
            newArray += [line[i2][i]]
        for i3 in range(len(newArray)):
            print(newArray[i3].ljust(lenCol,' '), end = "")
            print("|", end = "")
        print()
    print('-'*(lenCol + 1)*len(line))

def changeStr(str = ''):
    lenStr = 30
    arrayStr = []
    if len(str) > lenStr:
        i = 0
        while i <= len(str):
            arrayStr += [str[i:i+lenStr]]
            i += lenStr
        return arrayStr
    else:
        return [str]

def addArray(array = []):
    if type(array[0][0]) == str:
        min = len(array[0])
        max = 0
        for i in array:
            if len(i) > max:
                max = len(i)
            elif len(i) < min:
                min = len(i)
        if min != max:
            for i in range(len(array)):
                if len(array[i]) < max:
                    for k in range(max-min):
                        array[i] += ['']
    elif type(array[0]) == list:
        for i in range(len(array)):
            array[i] = addArray(array[i])
    return array

def listKeys(dictList):
    keyList = []
    for key in dictList:
        keyList += [key]
    return keyList

import pytest
def test_digit(string):
    with pytest.raises(ValueError):
        int(string)

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def testingType(line):
    # если значение - логический тип
    if is_digit(str(line)) == True:
        return str(line)
    else:
        if line == True:
            line = 'Yes'
            return line
        elif line == False:
            line = 'No'
            return line

    # если значение - список или  кортеж или множество
    if isinstance(line, (list, tuple, set)):
        if type(line[0]) == dict:
            newList = []
            for each in line:
                newList += [testingType(each)]
            line = newList
            return line
        else:
            line = [str(i) for i in line]
            return line

    # если значение - словарь
    if type(line) == dict:
        keyDict = listKeys(line)
        newVal = []
        for each in keyDict:
            newVal += [testingType(line.get(each))]
        line = newVal

    return(line)

def changeArr(line):
    arr = []
    for i in range(len(line)):
        arr += line[i]
    return arr

def readFile():
    #считывание файла
    try:
        fileName = 'data.json'
        fileOpen = open(fileName)
        try:
            import json
        except ImportError as e:
            import json
            print("Problem with import json")
        data = json.load(fileOpen)
        #список всех ключей
        keyList = listKeys(data[0].keys())
        # преобразование файла
        for eachPart in data:
            for key in keyList:
                eachPart[key] = testingType(eachPart[key])
                if type(eachPart[key]) == str:
                    eachPart[key] = changeStr(eachPart[key])
                elif type(eachPart[key]) == list:
                    for i in range(len(eachPart[key])):
                        if type(eachPart[key][i]) == list:
                            for i2 in range(len(eachPart[key][i])):
                                eachPart[key][i][i2] = changeStr(eachPart[key][i][i2])
                        else:
                            [eachPart[key][i]] = changeStr(eachPart[key][i])

        for eachKey in keyList:
            array = [[eachKey]]
            for eachPart in data:
                if type(eachPart[eachKey][0]) == list:
                    while (type(eachPart[eachKey][0]) != str):
                        eachPart[eachKey] = changeArr(eachPart[eachKey])
                array += [eachPart[eachKey]]
            my_print(addArray(array))

    except FileNotFoundError as e:
        print("File not found")
    except IOError as e:
        print("Problem with input or output")
    except (KeyError, IndexError) as e:
        print("Problem with keys or indexes")

readFile()
