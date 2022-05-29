import xlrd
import sqlite3

conn = sqlite3.connect('usersbase.db')
cur1 = conn.cursor()

def main():
    cur1.execute("DROP TABLE IF EXISTS elders;")
    conn.commit()
    cur1.execute("""CREATE TABLE IF NOT EXISTS elders(
       groupe TEXT,
       last_name TEXT,
       first_name TEXT,
       patronymic TEXT);
    """)
    conn.commit()

def go_to_elders():
    book = xlrd.open_workbook('C:/Users/Andrey/Desktop/first.xls',formatting_info=True)
    sheet_count = book.nsheets
    font = book.font_list

    for number_sheet in range(0,sheet_count):
        sheet = book.sheet_by_index(number_sheet)
        for column in range(1, sheet.ncols, 5):
            flag = True
            for row in range(0, sheet.nrows):
                cell_val = sheet.cell_value(row, column)
                cell_xf = book.xf_list[sheet.cell_xf_index(row, column)]
                tmp = cell_val, font[cell_xf.font_index].bold
                if tmp[1] == 1 and flag:
                    group = tmp[0]
                    flag = False
                elif tmp[1] == 1 and not flag:
                    l_name = tmp[0]
                    for fio in range(1, 3):
                        cell_val = sheet.cell_value(row, column + fio)
                        cell_xf = book.xf_list[sheet.cell_xf_index(row, column + fio)]
                        tmp = cell_val, font[cell_xf.font_index].bold
                        if fio == 1:
                            f_name = tmp[0]
                        if fio == 2:
                            patr = tmp[0]
                    elder = (group, l_name, f_name, patr)
                    cur1.execute('INSERT INTO elders values(?, ?, ?, ?)', elder)
                    conn.commit()
                    flag = True

def delete_null(gr = ""):
    cur1.execute(f"DELETE FROM elders WHERE groupe ={gr};")
    conn.commit()


def get_elder(group):
    cur1.execute(f"select last_name, first_name, patronymic from elders where groupe='{group}'")
    fio = ""
    for s in cur1:
        for i in range(0, 3):
            fio += f"{s[i]} "
    if fio == "":
        return "False"
    return fio

def try_elder(l_name, f_name, patr):
    cur1.execute(f"select * from elders where last_name='{l_name}' and first_name='{f_name}' and patronymic='{patr}'")
    for s in cur1:
        return "True"
    return "False"


if __name__ == "__main__":
    main()
    go_to_elders()
    delete_null()

