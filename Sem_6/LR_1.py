import pandas

data = pandas.read_csv('train.csv', index_col="PassengerId")

# print(type(data.at[100, False]))

def get_number_of_pass(data_file):
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    res = data['Sex'].value_counts()
    male_int, female_int = res['male'], res['female']
    return (male_int, female_int)



def get_port_stat(data_file):
    q_port_int = 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    res = data['Embarked'].value_counts()
    q_port_int = res['Q']
    return (q_port_int)


def get_survival_procent(data_file):
    surv_int = 0
    data = pandas.read_csv(data_file, index_col="PassengerId")
    res = data['Survived'].value_counts()
    surv_int = res[1]
    return ((surv_int * 100)/891)

def get_survival_corr(data_file):
    return (data['Survived'].corr(data['Fare'], method='pearson'))

print( get_number_of_pass('train.csv') )

print( get_port_stat('train.csv') )

print( get_survival_procent('train.csv') )

print( get_survival_corr('train.csv') )

