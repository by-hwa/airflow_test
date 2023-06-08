from airflow import DAG
from airflow.operators.python import PythonOperator

import datetime

default_args = {
    'owner': 'byeonghwa',
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=5)
}


# def greet(age, ti):
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print("Hello world! name{} {} \n and i am {} age".format(first_name, last_name, age))


def get_name(ti):
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Fridman')


def get_age(ti):
    ti.xcom_push(key='age', value='19')


with DAG(
    dag_id='our_dag_with_python_operator_v06',
    default_args=default_args,
    description='Our first dag using python',
    start_date=datetime.datetime(year=2023, month=3, day=16),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        # op_kwargs={'age':20}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1

