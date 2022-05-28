import pandas as pd

def try_group_with_flow(flow, group):
    file = pd.read_excel('C:/Users/Andrey/Desktop/first.xls', sheet_name=flow, header=None)
    len = file.shape[1]
    for i in range (0, len, 5):
        for s in (file.iloc[:, i+1:i+2]).to_numpy():
            if isinstance(s[0], str) and group in s[0]:
                return "True"
    return "False"

def try_group(group):
    names = ["поток И1", "поток И2", "поток И3", "поток А1 (1,2,3,4)", "поток А1 (5,6)",
             "поток А2", "поток А3", "поток М1", "поток М2", "поток М(Пр)", "поток М3",
             "Поток Э"]
    files = pd.read_excel('C:/Users/Andrey/Desktop/first.xls', sheet_name=names, header=None)
    for name in names:
        len = files[name].shape[1]
        for i in range(0, len, 5):
            s = (files[name].iloc[:, i + 1:i + 2]).to_numpy()
            for st in s:
                if isinstance(st[0], str) and group in st[0]:
                    return "True"
    return "False"

def try_student(group, last_name, first_name, patronymic):
    names = ["поток И1", "поток И2", "поток И3", "поток А1 (1,2,3,4)", "поток А1 (5,6)",
             "поток А2", "поток А3", "поток М1", "поток М2", "поток М(Пр)", "поток М3",
             "Поток Э"]
    files = pd.read_excel('C:/Users/Andrey/Desktop/first.xls', sheet_name=names, header=None)
    for name in names:
        if try_group_with_flow(name, group) == "True":
            len = files[name].shape[1]
            flag = False
            for i in range (0, len, 5):
                s = (files[name].iloc[:, i+1:i+4]).to_numpy()
                for st in s:
                    if (not flag) and isinstance(st[0], str) and group in st[0]:
                        flag = True
                    if flag:
                        if not isinstance(st[0], str):
                            flag = False
                        else:
                            if last_name in st[0] and first_name in st[1] and isinstance(st[2], str) \
                                    and patronymic in st[2]:
                                return "True"
    return "False"

def check_valid_reg(mail_in, group_in, l_name, f_name, patr):
    if not ('.' and '@' in mail_in):
        return "Некорректный mail"
    if try_student(group_in, l_name, f_name, patr) == "True":
        return "True"
    else:
        return "Студента с таким ФИО в указанной группе нет"


if __name__ == "__main__":
#print(try_group("АДБ-21-05"))
#print(find_group("поток И2", "ИДБ-21-05"))
    print(try_student("ИДБ-21-05", "Гаффоров", "Абдусамад", "Абдукодирович"))