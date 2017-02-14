"""
Code that goes along with the Airflow tutorial located at:
https://github.com/airbnb/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.sensors import HttpSensor
from wecashdag.dags.batchjobenum import BatchJobEnum
from wecashdag.dags.util import dagutil

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

# taskid = 'testtaskid1'

taskid = dagutil.getseqnum(BatchJobEnum.JinShangMeltStatusCancel.value)
payload = {'taskType': 1, 'scheduleNumber': taskid, 'capitalId': '1'}

with DAG('httpdag', start_date=datetime(2016, 1, 1), schedule_interval='*/1 * * * *') as dag:
    (
        dag
        >> PythonOperator(
            task_id='python_1',
            python_callable=lambda: dagutil.do_post(
                "http://capital-dev.wecash.net/zfpt/batchjob/trigger/cancelCapitalMelt", payload))
        >> HttpSensor(
            task_id='http_sensor_check',
            http_conn_id='localtest',
            endpoint='',
            params={"taskType": "1", "scheduleNumber": taskid},
            # response_check=lambda response: True if "Google" in response.content else False,
            response_check=lambda response: dagutil.parse_get_result(response),
            poke_interval=5,
            timeout=30,
            dag=dag)
    )

if __name__ == '__main__':

    try:
        print("main")
    except KeyboardInterrupt:
        print("exception")

    pass
