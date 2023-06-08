from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.trino.operators.trino import TrinoOperator
from airflow.providers.trino.hooks.trino import TrinoHook