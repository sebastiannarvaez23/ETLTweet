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
import time

def main():
    database = mysql.ConnMySQL()
    api = apitweet.TweeterAPI()
    tweets = api.get_all_tweets("Medio ambiente petro", 100)
    print(tweets)

    for tweet in tweets:
        database.insert_teewt(tweet)

if __name__ == "__main__":
    main()