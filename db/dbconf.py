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
        #rint("Conecction Succesfull!")

    def insert_teewt(self, tweet):
        sql = query_insert_tweet(tweet)
        try:
            self.connection.ping()
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise print(f"hubo un porblema: {e}")
    
    def close(self):
        self.connection.close()
