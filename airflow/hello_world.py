"""
Airflow tag demo
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

import logging
logging._Level = logging.DEBUG

default_args = {
    "owner": "smiecj",
    "start_date": datetime(2021, 7, 21)
}

dag = DAG("Hello-World", 
        description="My first dag",
        default_args=default_args, 
        schedule_interval='0 * * * *')

t1 = BashOperator(task_id="hello", bash_command="echo 'Hello World, today is {{ ds }}'", dag=dag)