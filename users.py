import sqlite3

conn = sqlite3.connect('usersbase.db')
cur = conn.cursor()

def main():
    cur.execute("DROP TABLE IF EXISTS users;")
    conn.commit()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       mail TEXT,
       groupe TEXT,
       last_name TEXT,
       first_name TEXT,
       patronymic TEXT,
       password TEXT);
    """)
    conn.commit()


def find_user(mail_in):
    cur.execute("SELECT mail FROM users;")
    for e in cur:
        if e[0] == mail_in:
            return True
    return False

def find_group(mail_in):
    cur.execute(f"select groupe from users where mail='{mail_in}'")
    for e in cur:
        return e[0]
    return False

def go_to_base(mail_in, group_in, l_name, f_name, patr, passwrd):
    user = (mail_in, group_in, l_name, f_name, patr, passwrd)
    cur.execute('INSERT INTO users values(?, ?, ?, ?, ?, ?)', user)
    conn.commit()

def delete_user(mail_in):
    cur.execute(f"DELETE FROM users WHERE mail='{mail_in}';")
    conn.commit()

def delete_database():
    cur.execute("DELETE FROM users;")
    conn.commit()

if __name__ == "__main__":
    main()
    #go_to_base("mail_in", "group_in", "f_name", "l_name", "patr", "passwrd")
    #("mail_in")