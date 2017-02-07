"""
Code that goes along with the Airflow tutorial located at:
https://github.com/airbnb/airflow/blob/master/airflow/example_dags/tutorial.py
"""
import requests
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

from wecashdag.requests.requests import HTTPPost

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('Test', default_args=default_args)
http = HTTPPost

with DAG('my_dag', start_date=datetime(2016, 1, 1), schedule_interval='*/1 * * * *') as dag:
    (
    dag
        >> DummyOperator(task_id='dummy_1')
        >> BashOperator(
            task_id='bash_1',
            bash_command='echo "HELLO!"')
        >> PythonOperator(
            task_id='python_1',
            python_callable=lambda: HTTPPost.doPost(http))
    )


def do_post():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://localhost:8000", data=payload)
    print(r.text)
