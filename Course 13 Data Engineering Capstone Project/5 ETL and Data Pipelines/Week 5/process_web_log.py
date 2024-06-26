
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Ankit Sharma',
    'start_date': days_ago(0),
    'email': ['ankit@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# define the DAG
dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='Capstone Project ETL DAG using Bash',
    schedule_interval=timedelta(days=1),
)

# define the task named extract_data to call the shell script
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d " " -f1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    dag=dag,
)
# define the task named transform_data to call the shell script to filter ipaddress "198.46.149.143"

transform_data = BashOperator(
    task_id='transform_data',
    bash_command='cat /home/project/airflow/dags/capstone/extracted_data.txt | grep "198.46.149.143" > /home/project/airflow/dags/capstone/transformed_data.',
    dag=dag,
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf /home/project/airflow/dags/capstone/weblog.tar /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag,
)
# task pipeline
extract_data >> transform_data >> load_data