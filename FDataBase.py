import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()



    def GetMenu(self):
        try:
            self.__cur.execute(f"SELECT * FROM  mainmenu")
            res = self.__cur.fetchall()
            return res
        except:
            print("ошибка чтения из БД")
        return ['fail']


    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print('Ошибка получения данных из БД' + str(e))
        return False



    def getUserByUsers(self, user):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE users = '{user}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print('Ошибка получения данных из БД' + str(e))
        return False