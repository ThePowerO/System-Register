import sys
from PyQt5 import QtWidgets, uic
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

def sing_with():
    email = window.lineEdit.text()
    password = window.lineEdit_2.text()

    try:
        bank = sqlite3.connect("data_user.db")
        cursor = bank.cursor()

        cursor.execute(f"SELECT password FROM data_user WHERE email='{email}'")

        caught_password = cursor.fetchall()

        try:
            if password == caught_password[0][0]:
                print("Joined")
            else:
                print("Didn't entered")
        except:
            pass            
        
    except sqlite3.Error as error:
        print(error)

    window.lineEdit.setText("")
    window.lineEdit_2.setText("")

app = QtWidgets.QApplication([])
window = uic.loadUi("InterfaceSys.ui")

window.pushButton.clicked.connect(sing_with)
window.pushButton_2.clicked.connect(lambda: window.windowns.setCurrentWidget(window.Register))
window.pushButton_4.clicked.connect(lambda: window.windowns.setCurrentWidget(window.Login))

window.show()
sys.exit(app.exec_())
