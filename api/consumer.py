from api.credentials import ACCESS_TOKEN_SECRET
import tweepy

"""
Test Data:
query = 'covid -is:retweet'
response = client.search_recent_tweets(query=query, max_results=100)
"""

client = tweepy.Client(bearer_token=ACCESS_TOKEN_SECRET)

class TweeterAPI:

    def get_all_tweets(self, query):
        global client
        tweets = []
        for tweet in tweepy.Cursor(client.search, q=query, tweet_mode="extended").items(100):
            print("El texto es " + tweet.text)
            print("Fecha de creacion " + tweet.created_at)
            print("Numero de favoritos " + tweet.favorite_count)
            print("Numero de retweets " + tweet.retweet_count)
            print("Coordenadas del tweet " + tweet.coordinates)

            tweets.append({
                'text': tweet.text,
                'created_at': tweet.created_at,
                'favorite_count': tweet.favorite_count,
                'retweet_count': tweet.retweet_count,
                'coordinates': tweet.coordinates,
            })
        return tweets