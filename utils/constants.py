import configparser
import os

parser = configparser.ConfigParser()
configPath = os.path.join(os.path.dirname(__file__), '../config/config.conf') #root_dir/config/config.conf
parser.read(configPath)


SECRET = parser.get(section='api_keys', option='reddit_secret_key')
CLIENT_ID = parser.get(section='api_keys', option='reddit_client_id')

DATABASE_HOST =  parser.get(section='database', option='database_host')
DATABASE_NAME =  parser.get(section='database', option='database_name')
DATABASE_PORT =  parser.get(section='database', option='database_port')
DATABASE_USER =  parser.get(section='database', option='database_username')
DATABASE_PASSWORD =  parser.get(section='database', option='database_password')

#GET AWS CREDS
AWS_ACCESS_KEY_ID = parser.get(section='aws', option='aws_access_key_id')
AWS_SECRET_KEY = parser.get(section='aws', option='aws_secret_access_key')
AWS_REGION = parser.get(section='aws', option='aws_region')
AWS_BUCKET_NAME = parser.get(section='aws', option='aws_bucket_name')

INPUT_PATH = parser.get(section='file_paths', option='input_path')
OUTPUT_PATH = parser.get(section='file_paths', option='output_path')

# Log sample of a reddit Post object: {'comment_limit': 2048, 'comment_sort': 'confidence', '_reddit': <praw.reddit.Reddit object at 0xffff82f66910>, 'approved_at_utc': None, 'subreddit': Subreddit(display_name='dataengineering'), 'selftext': 'https://www.databricks.com/blog/databricks-tabular', 'author_fullname': 't2_cqao8', 'saved': False, 'mod_reason_title': None, 'gilded': 0, 'clicked': False, 'title': 'Databricks acquires Tabular', 'link_flair_richtext': [], 'subreddit_name_prefixed': 'r/dataengineering', 'hidden': False, 'pwls': 6, 'link_flair_css_class': '', 'downs': 0, 'thumbnail_height': None, 'top_awarded_type': None, 'hide_score': False, 'name': 't3_1d8118g', 'quarantine': False, 'link_flair_text_color': 'light', 'upvote_ratio': 0.98, 'author_flair_background_color': None, 'subreddit_type': 'public', 'ups': 173, 'total_awards_received': 0, 'media_embed': {}, 'thumbnail_width': None, 'author_flair_template_id': None, 'is_original_content': False, 'user_reports': [], 'secure_media': None, 'is_reddit_media_domain': False, 'is_meta': False, 'category': None, 'secure_media_embed': {}, 'link_flair_text': 'Discussion', 'can_mod_post': False, 'score': 173, 'approved_by': None, 'is_created_from_ads_ui': False, 'author_premium': False, 'thumbnail': 'self', 'edited': False, 'author_flair_css_class': None, 'author_flair_richtext': [], 'gildings': {}, 'post_hint': 'self', 'content_categories': None, 'is_self': True, 'mod_note': None, 'created': 1717517504.0, 'link_flair_type': 'text', 'wls': 6, 'removed_by_category': None, 'banned_by': None, 'author_flair_type': 'text', 'domain': 'self.dataengineering', 'allow_live_comments': False, 'selftext_html': '<!-- SC_OFF --><div class="md"><p><a href="https://www.databricks.com/blog/databricks-tabular">https://www.databricks.com/blog/databricks-tabular</a></p>\n</div><!-- SC_ON -->', 'likes': None, 'suggested_sort': None, 'banned_at_utc': None, 'view_count': None, 'archived': False, 'no_follow': False, 'is_crosspostable': False, 'pinned': False, 'over_18': False, 'preview': {'images': [{'source': {'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?auto=webp&s=3d1dbb9eb4567b595b09a2c4ab79e99733275803', 'width': 1200, 'height': 628}, 'resolutions': [{'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?width=108&crop=smart&auto=webp&s=b84644c4d6543a2adbc8d9be1014afd9c757041e', 'width': 108, 'height': 56}, {'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?width=216&crop=smart&auto=webp&s=1e33c8b6a6cf151a1ac2a7c6f036efcb225e66b8', 'width': 216, 'height': 113}, {'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?width=320&crop=smart&auto=webp&s=065a2897d2a50f6eda15b6fb4b342dabe6506c1d', 'width': 320, 'height': 167}, {'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?width=640&crop=smart&auto=webp&s=df4a3ebb584e3a4ba07dea46b026c356b155607c', 'width': 640, 'height': 334}, {'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?width=960&crop=smart&auto=webp&s=10bd7882f338cab807d7f974aad4bc2720377cc0', 'width': 960, 'height': 502}, {'url': 'https://external-preview.redd.it/AIrGfRgf_b_kylATL05Oolsfw7zRvONIXqMyffTxckA.jpg?width=1080&crop=smart&auto=webp&s=64bf31b836d0c8f3e1b81db6a565e942e4f2debd', 'width': 1080, 'height': 565}], 'variants': {}, 'id': 'N152Gho5EKv55Wck64WuBIBCDKz1itMsLbzYZu2zeyM'}], 'enabled': False}, 'all_awardings': [], 'awarders': [], 'media_only': False, 'link_flair_template_id': '92b74b58-aaca-11eb-b160-0e6181e3773f', 'can_gild': False, 'spoiler': False, 'locked': False, 'author_flair_text': None, 'treatment_tags': [], 'visited': False, 'removed_by': None, 'num_reports': None, 'distinguished': None, 'subreddit_id': 't5_36en4', 'author_is_blocked': False, 'mod_reason_by': None, 'removal_reason': None, 'link_flair_background_color': '#ff4500', 'id': '1d8118g', 'is_robot_indexable': True, 'report_reasons': None, 'author': Redditor(name='dan_the_lion'), 'discussion_type': None, 'num_comments': 93, 'send_replies': True, 'whitelist_status': 'all_ads', 'contest_mode': False, 'mod_reports': [], 'author_patreon_flair': False, 'author_flair_text_color': None, 'permalink': '/r/dataengineering/comments/1d8118g/databricks_acquires_tabular/', 'parent_whitelist_status': 'all_ads', 'stickied': False, 'url': 'https://www.reddit.com/r/dataengineering/comments/1d8118g/databricks_acquires_tabular/', 'subreddit_subscribers': 188236, 'created_utc': 1717517504.0, 'num_crossposts': 0, 'media': None, 'is_video': False, '_fetched': False, '_additional_fetch_params': {}, '_comments_by_id': {}}

# sampling a few interesting fields below
POST_FIELDS = (
    'id',
    'title',
    'score',
    'selftext',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)
