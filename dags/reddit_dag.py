from airflow import DAG
from datetime import datetime
import os 
import sys
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # to set REDDIT_ETL_PIPELINE as root folder

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner' : 'Mohith',
    'start_date' : datetime(2024, 6, 3)   
}

file_postfix = datetime.now().strftime("%Y%m%d") # format that will be appended to the file names

dag = DAG(
    dag_id = "reddit_etl_pipeline",
    default_args = default_args,
    schedule_interval= '@daily',
    catchup = False,
    tags = ['reddit' , 'etl', 'pipeline']
)

# extract from Reddit

extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_{file_postfix}', # reddit_%Y%m%d
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100 #fetch 100 posts in a subreddit for a particular date
    },
    dag=dag
)

# upload to S3

upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3