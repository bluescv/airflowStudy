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

from airflow.operators.sensors import HttpSensor

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

with DAG('httpdag', start_date=datetime(2016, 1, 1), schedule_interval='*/1 * * * *') as dag:
    (
        dag
        >> HttpSensor(
            task_id='http_sensor_check',
            http_conn_id='localtest',
            endpoint='',
            params={},
            # response_check=lambda response: True if "Google" in response.content else False,
            response_check=lambda response: parse_get_result(response),
            poke_interval=5,
            timeout=30,
            dag=dag)
    )


def do_post():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://localhost:8000", data=payload)
    print(r.text)


def parse_get_result(response):
    print("Inside parse_get_result")
    return False