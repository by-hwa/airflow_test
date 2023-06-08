from airflow import DAG
from airflow.operators.bash import BashOperator

import datetime

default_args = {
    'owner': 'byeonghwa',
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=5)
}

with DAG(
    dag_id='our_first_dag_v4',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime.datetime(year=2023, month=3, day=16),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, i am task2 and will be running after task1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hey, i am task3 and will be running after task1 at the same time as the task2 "
    )

    # Task dependency method1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method2
    task1 >> [task2, task3]
