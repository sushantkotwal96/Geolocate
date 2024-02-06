from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import task
from airflow.utils.dates import days_ago
import os
import sys

PROJECT_ROOT = os.path.abspath(__file__ + "/../../../")
sys.path.append(PROJECT_ROOT)

dag = DAG(dag_id = 'data_ingestion_dag',
          default_args={'owner':'vishwa',
                        'retries':0,
                        'start_date':days_ago(1)},
            description="Data Ingestion service"
        )

def run_twitter_etl_service():
    from services.data_ingestion.twitter_etl import run_twitter_etl_pipeline
    league = 'premierleague'
    n_tweets = 100
    run_twitter_etl_pipeline(league, n_tweets)



with dag:
    data_ingestion_task = PythonOperator(
        task_id = 'twitter_etl_task',
        python_callable = run_twitter_etl_service
    )
    data_ingestion_task