from api.credentials import ACCESS_TOKEN_SECRET, API_KEY, API_KEY_SECRET, ACCESS_TOKEN
from textblob.classifiers import NaiveBayesClassifier
import tweepy

class TweeterAPI:
    def get_all_tweets(self, query, limit):

        with open('api/traininginput.json', 'r') as fp:
            cl=NaiveBayesClassifier(fp, format='json')

        response = []
        auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        for tweet in tweepy.Cursor(api.search_tweets, q=query).items(limit):
            classification = cl.classify(tweet.text)
            response.append({
                'id_tweet':tweet.id,
                'text':tweet.text,
                'created_date':tweet.created_at,
                'favorites':tweet.favorite_count,
                'retweets':tweet.retweet_count,
                'classification': classification
            })
        return response

        