
def query_insert_tweet(tweet):
    sql = f"""
    INSERT INTO tweets 
    (id_tweet, text_tweet, created_date, favorites, retweets, classification) 
    VALUES 
    ('{tweet['id_tweet']}', '{tweet['text']}', '{tweet['created_date']}', '{tweet['favorites']}', '{tweet['retweets']}', '{tweet['classification']}')
    """
    return sql