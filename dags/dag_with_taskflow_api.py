from airflow.decorators import dag, task
import datetime

default_args = {
    'owner': 'leebyeonghwa',
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=5)
}

@dag(
    dag_id='dag_with_taskflow_api_v02',
    default_args=default_args,
    start_date=datetime.datetime(year=2023, month=3, day=20),
    schedule_interval='@daily'
)
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Fridnam'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print("hello world! my name is {} {}, and i am {} years old".format(first_name, last_name, age))

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'],
          age=age)


greet_dag = hello_world_etl()