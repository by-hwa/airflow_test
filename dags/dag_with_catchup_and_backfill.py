from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

default_args = {
    'owner': 'leebyeonghwa',
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=4)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v01',
    default_args=default_args,
    start_date=datetime.datetime(year=2023, month=3, day=1),
    schedule_interval='@daily',
    catchup=True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )