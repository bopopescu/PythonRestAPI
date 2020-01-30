import mysql.connector as mysql

class DBManager:

    @staticmethod
    def initdb():
        db = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="dutch@123",
            database="StockBroker"
        )
        return db