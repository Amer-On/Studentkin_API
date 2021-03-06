import re
import pandas as pd

def check_email(email):
	pattern = r"\d{6}@stud.stankin.ru"
	if re.match(pattern, email) is not None:
		return "valid"
	return "invalid"


def try_group(group):
    names = ["поток И1", "поток И2", "поток И3", "поток А1 (1,2,3,4)", "поток А1 (5,6)",
             "поток А2", "поток А3", "поток М1", "поток М2", "поток М(Пр)", "поток М3",
             "Поток Э"]
    files = pd.read_excel('first.xls', sheet_name=names, header=None)
    for name in names:
        len = files[name].shape[1]
        for i in range(0, len, 5):
            s = (files[name].iloc[:, i + 1:i + 2]).to_numpy()
            for st in s:
                if isinstance(st[0], str) and group in st[0]:
                    return True
    return False

def try_group_with_flow(flow, group):
    file = pd.read_excel('first.xls', sheet_name=flow, header=None)
    len = file.shape[1]
    for i in range (0, len, 5):
        for s in (file.iloc[:, i+1:i+2]).to_numpy():
            if isinstance(s[0], str) and group in s[0]:
                return True
    return False


def try_student(group, last_name, first_name, patronymic):
    names = ["поток И1", "поток И2", "поток И3", "поток А1 (1,2,3,4)", "поток А1 (5,6)",
             "поток А2", "поток А3", "поток М1", "поток М2", "поток М(Пр)", "поток М3",
             "Поток Э"]
    files = pd.read_excel('first.xls', sheet_name=names, header=None)
    for name in names:
        if try_group_with_flow(name, group) == True:
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
                                return True
    return False
