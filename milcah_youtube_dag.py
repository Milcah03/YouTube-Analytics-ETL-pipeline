from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import subprocess
import pendulum

# Set timezone to EAT Nairobi
nairobi_tz = pendulum.timezone("Africa/Nairobi")

default_args = {
    'owner': 'milcah',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define Python callables
def run_extraction():
    subprocess.run(
        ['/home/luxde/milcah/YouTube-Project/venv/bin/python', '/home/luxde/milcah/YouTube-Project/youtube_extract.py'],
        check=True
    )

def run_transformation():
    subprocess.run(
        ['/home/luxde/milcah/YouTube-Project/venv/bin/python', '/home/luxde/milcah/YouTube-Project/youtube_transform.py'],
        check=True
    )

def run_load():
    subprocess.run(
        ['/home/luxde/milcah/YouTube-Project/venv/bin/python', '/home/luxde/milcah/YouTube-Project/youtube_load.py'],
        check=True
    )

# Define the DAG
with DAG(
    dag_id='milcah_youtube_analytics_pipeline',
    default_args=default_args,
    description='YouTube Analytics ETL DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 1, tzinfo=nairobi_tz),
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='run_extraction',
        python_callable=run_extraction
    )

    transform_task = PythonOperator(
        task_id='run_transformation',
        python_callable=run_transformation
    )

    load_task = PythonOperator(
        task_id='run_load',
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task
