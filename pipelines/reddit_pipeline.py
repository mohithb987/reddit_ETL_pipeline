import pandas as pd
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH

def reddit_pipeline(file_name: str, subreddit: str, time_filter: 'day', limit: None ):
    # connect to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'My Agent')
    # EXTRACTION
    posts = extract_posts(instance, subreddit, time_filter, limit)
    
    posts_df = pd.DataFrame(posts)
    
    # TRANSFORMATION
    
    post_df = transform_data(posts_df)

    # LOAD TO CSV
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, path= file_path)

    return file_path