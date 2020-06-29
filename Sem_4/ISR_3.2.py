class Record(): # класс запись
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        def show_comment(self, comment=object):
            print(f"Заголовок коммента: {comment.title}, текст коммента: {comment.text}")

class Comment(): # класс комментарий (наследует класс запись)
    def __init__(self, nickname, textcom):
        self.__nickname = nickname
        self.__textcom = textcom

# Геттеры и сеттеры для поля text
 @property
 def text(self):
     return self.__text
    
 @text.setter
 def text(self, value):
     self.__title = str(value)

 @text.deleter
 def text(self):
     self.__text = None

# Геттеры и сеттеры для поля textcom 
 @property
 def textcom(self):
     return self.__textcom
    
 @textcom.setter
 def textcom(self, value):
     self.__textcom = str(value)

 @textcom.deleter
 def textcom(self):
     self.__textcom = None

 def show(self):   #Создание функций для вывода на печать информации, хранящийся в объектах.   
     print("author: " + str(self.author))
     print("text: " + str(self._text))
