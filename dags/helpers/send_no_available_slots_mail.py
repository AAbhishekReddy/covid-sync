import json
from jinja2 import Template

from airflow.utils.email import send_email


HTML_content = """
<!DOCTYPE html>
<html lang="en">

<body>
    <div align="center">
        <h1 style="font-family: 'Courier New', Courier, monospace; font-size: 35px;">No Available Vaccination Centers</h1>
        <h2 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">There are no available vaccination centers for your selected age group.</h2>
    </div>
</body>


</html>
"""


def send_no_available_slots_mail(**kwargs):
    recipient_address = kwargs["email"]
    subject = "No Available Vaccination Centers"

    send_email(recipient_address, subject, HTML_content)
