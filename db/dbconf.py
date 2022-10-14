from db.queries import query_insert_tweet
import pymysql

class ConnMySQL:
    def __init__(self):
        """
        Constructor that allows to initiate a connection with the database
        """
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='apibigdata',
        )
        self.cursor = self.connection.cursor()
        print("Conecction Succesfull!")

    def insert_teewt(self, tweet):
        sql = query_insert_tweet(tweet)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    
    def close(self):
        self.connection.close()
