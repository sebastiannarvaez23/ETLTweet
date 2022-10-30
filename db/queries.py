
def format_text_for_query(text):
    new_text = text.replace("'", "\"")
    return new_text

def query_insert_tweet(tweet):
    sql = f"""
    INSERT INTO tweets 
    (id_tweet, text_tweet, created_date, favorites, retweets, classification) 
    VALUES 
    ('{tweet['id_tweet']}', '{format_text_for_query(tweet['text'])}', '{tweet['created_date']}', '{tweet['favorites']}', '{tweet['retweets']}', '{tweet['classification']}')
    """
    return sql