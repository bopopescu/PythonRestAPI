import mysql.connector as mysql


class DBManager:
    db = "empty object"

    @staticmethod
    def initdb():
        global db
        db = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="dutch@123",
            database="StockBroker"
        )
        return db

    @staticmethod
    def executequery(query):
        global db
        cursor = db.cursor()

        cursor.execute(query)
        cursor.fetchall()
        return cursor
