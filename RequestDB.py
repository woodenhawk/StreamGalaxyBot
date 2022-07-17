import sqlite3

con = sqlite3.connect("DB\DB.db")
cursor = con.cursor()

def SelectService():
    data = cursor.execute("SELECT * FROM Service")
    return data

def InsertUser(IdChat):
    data = con.execute("SELECT COUNT(*) FROM User WHERE IdChat = ?", (IdChat, ))
    if data.fetchone()[0] > 0:
        print("Такой пользователь уже зарегистрирован")
        return

    con.execute("INSERT INTO User (IdChat) VALUES (?);", (IdChat, ))
    con.commit()
    print("Добавлена строка в User")

def ServiceUser(IdChat, IdService, Date):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat, ))
    IdUser = data.fetchone()[0]
    con.execute("INSERT INTO ServiceUser (IdService, IdUser, Date) VALUES (?,?,?)", (IdService, IdUser, Date))
    con.commit()
    print("Добавлена строка в ServiceUser")

def UpdateServiceUser(Date, IdChat):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat, ))
    IdUser = data.fetchone()[0]
    con.execute("UPDATE ServiceUser SET Date=? Where IdUser =? and Date=?", (Date, IdUser, 'Без даты'))
    con.commit()
    print("Обновлено значение в ServiceUser")

def UpdateNameUser(Name, IdChat):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat,))
    IdUser = data.fetchone()[0]
    con.execute("UPDATE User SET Name=? Where IdChat =?", (Name, IdChat))
    con.commit()
    print("Добавил имя пользователю")

def UpdateEmailUser(Email, IdChat):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat,))
    IdUser = data.fetchone()[0]
    con.execute("UPDATE User SET Email=? Where IdChat =?", (Email, IdChat))
    con.commit()
    print("Добавил email пользователю")

def UpdatePhoneUser(Phone, IdChat):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat,))
    IdUser = data.fetchone()[0]
    con.execute("UPDATE User SET Phone=? Where IdChat =?", (Phone, IdChat))
    con.commit()
    print("Добавил телефон пользователю")

def SelectUser(IdChat):
    data = con.execute("SELECT * FROM User Where IdChat=?", (IdChat,))
    list = data.fetchone()
    return list

def Application(IdChat):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat,))
    IdUser = data.fetchone()[0]
    data = con.execute("SELECT IdService FROM ServiceUser WHERE IdUser=? order by id desc limit 1", (IdUser,))
    IdService = data.fetchone()[0]
    data = con.execute("SELECT * FROM Service Where IdService = ?", (IdService,))
    list = data.fetchone()
    return list

def SelectServiceUser(IdChat):
    data = con.execute("SELECT Id FROM User WHERE IdChat = ?", (IdChat,))
    IdUser = data.fetchone()[0]
    data = con.execute("SELECT * FROM ServiceUser WHERE IdUser=? order by id desc limit 1", (IdUser,))
    ServiceUser = data.fetchone()
    return ServiceUser