import sqlite3

def register_new_user(name, email, password, confirm_password):
    erro = False

    if name:
        pass

    if '@' in email and '.com':
        pass

    if password == confirm_password and len(password) > 6:
        pass

    else:
        erro = True
    
    try:
        bank = sqlite3.connect("data_user.db")
        cursor = bank.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS data_user (name text, email text, password text)")
        cursor.execute(f"INSERT INTO data_user VALUES ('{name}', '{email}', '{password}')")

        bank.commit()
        bank.close()

    except sqlite3.Error as error:
        print(error)
        erro = True
    
    return erro

if not register_new_user("Exemple", "exemple@gmail.com", "exemple123", "exemple123"):
    print("Successfully Registered")
else:
    print("Register went wrong")