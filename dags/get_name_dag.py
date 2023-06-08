from airflow import DAG
from airflow.operators.python import PythonOperator

import datetime

default_args = {
    'owner': 'byeonghwa',
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=5)
}


def greet(name, age):
    print("Hello world! name{} age{}".format(name, age))


def get_name():
    return 'jerry'


with DAG(
    dag_id='our_dag_with_python_operator_v03',
    default_args=default_args,
    description='Our first dag using python',
    start_date=datetime.datetime(year=2023, month=3, day=16),
    schedule_interval='@daily'
) as dag:
    # task1 = PythonOperator(
    #     task_id='greet',
    #     python_callable=greet,
    #     op_kwargs={'name':'tom', 'age':20}
    # )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )

    task2

