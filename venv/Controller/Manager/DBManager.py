class DBManager:

    @staticmethod
    def initdb(self):
        db = mysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="dutch@123",
            database="TestDb"
        )
        return db