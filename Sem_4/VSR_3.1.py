class Conf():
  log = []
  def __init__(self, dicts):
    self.first_name = dicts["first_name"] 
    self.second_name = dicts["second_name"]
    self.phone = dicts["phone"]

  def otvetinfo(self):
     self.info = {
      "first_name": self.first_name,
      "second_name": self.second_name,
      "phone": self.phone,
    }

     return self.participant_info

first_name = input("Введите имя:")
second_name = input("Введите фамилию:")
phone = input("Телефон:")

info={"first_name":first_name,"second_name":second_name,"phone":phone}

stringinfo=Conf(info)
print(stringinfo.info())
