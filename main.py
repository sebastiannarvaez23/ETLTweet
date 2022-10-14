"""
    Santiago de Cali University

    Students:
    - Paula Andrea Moreno
    - Sebastian Narvaez
    - Ricardo Ruiz
    - Joan Villamarin

    Teacher:
    - Gustavo Alomia

    BIG DATA
"""
import db.dbconf as mysql
import api.consumer as apitweet

def main():
    database = mysql.ConnMySQL()
    api = apitweet.TweeterAPI()
    tweets = api.get_all_tweets("hola")
    for tweet in tweets:
        database.insert_teewt(tweet)

if __name__ == "__main__":
    main()