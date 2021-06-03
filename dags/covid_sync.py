from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.email import send_email

from helpers.get_slots import get_slots
from helpers.mail_notification import mail_notification

default_args = {
    'owner': 'ghost',
    'depends_on_past': False,
    'start_date': datetime(2021, 5, 22),
    'retries': 1
}

dag = DAG(dag_id="covid_sync", default_args=default_args,
          catchup=False, schedule_interval='15 1 * * *')


with dag:

    get_centers = PythonOperator(
        task_id="get_centers",
        python_callable=get_slots,
        provide_context=True,
        email_on_failure=True,
        email="annemabhishekreddy@gmail.com"
    ),

    send_notification = PythonOperator(
        task_id="send_notification",
        python_callable=mail_notification,
        provide_context=True,
        email_on_failure=True,
        email="annemabhishekreddy@gmail.com"
    )

    get_centers >> send_notification
