from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.configuration import conf

import logging
LOGGER = logging.getLogger(__name__)


default_args = {
    "owner": "smiecj",
    "start_date": datetime(2021, 7, 21)
}

dag = DAG("execute_bash_test",
        description="bash dag",
        default_args=default_args,
        schedule_interval='0 * * * *')

LOGGER.info(conf.get("core", "my_key"))

t1 = BashOperator(task_id="hello", bash_command="echo 'Hello World, today is {{ ds }}'", dag=dag)