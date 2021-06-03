from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.email import send_email

from helpers.get_slots import get_slots
from helpers.mail_notification import mail_notification
from helpers.check_available_centers import check_available_centers
from helpers.send_no_available_slots_mail import send_no_available_slots_mail


# ------------------ Enter Your email and your district ID here ------------------ #
email = "example@gmail.com"
district_id = "8"
min_age = 18
# ------------------------------------- end -------------------------------------- #


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
        op_kwargs={"district_id": district_id, "min_age": min_age},
        email_on_failure=True,
        email="covid.sync.mail@gmail.com"
    ),

    check_centers = BranchPythonOperator(
        task_id="check_centers",
        provide_context=True,
        python_callable=check_available_centers,
        op_kwargs={"email": email},
        email_on_failure=True,
        email="covid.sync.mail@gmail.com"
    )

    send_notification = PythonOperator(
        task_id="send_notification",
        python_callable=mail_notification,
        provide_context=True,
        op_kwargs={"email": email},
        email_on_failure=True,
        email="covid.sync.mail@gmail.com"
    )

    send_empty_slots_notification = PythonOperator(
        task_id="send_empty_slots_notification",
        python_callable=send_no_available_slots_mail,
        provide_context=True,
        op_kwargs={"email": email},
        email_on_failure=True,
        email="covid.sync.mail@gmail.com"
    )

    get_centers >> check_centers >> [send_notification, send_empty_slots_notification]
