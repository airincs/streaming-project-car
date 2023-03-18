from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from car_stream import run_car_stream

default_args = {
    'owner': 'airinfisher98',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 18),
    'email': ['airinfisher98@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'car_dag',
    default_args=default_args,
    description='Car Streaming Dag',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_car_stream',
    python_callable=run_car_stream,
    dag=dag, 
)

run_etl