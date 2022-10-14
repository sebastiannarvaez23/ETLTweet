
def query_insert_tweet(tweet):
    sql = """
    INSERT INTO tweets 
    (text, created_at, favorite_count, retweet_count, coordinates) 
    VALUES 
    ('{}', '{}', '{}', '{}', '{}')
    """.format(
        tweet.text, 
        tweet.created_at, 
        tweet.favorite_count, 
        tweet.retweet_count, 
        tweet.coordinates
    )
    
    return sql