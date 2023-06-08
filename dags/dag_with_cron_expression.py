from airflow import DAG
from airflow.operators.bash import BashOperator

import datetime

default_args = {
    'owner': 'leebyeonghwa',
    'retries': 5,
    'retry_delay': datetime.timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_v02",
    start_date=datetime.datetime(year=2023, month=3, day=1),
    schedule_interval='0 3 * * Tue' # crontab.guru 여러요일에 하고싶은 경우 쉼표로 추가 가능.
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo dag with cron expression!'
    )
    task1