import json
from jinja2 import Template

from airflow.utils.email import send_email


template_html = """
<!DOCTYPE html>
<html lang="en">

<body>
    <div align="center">
        <h1 style="font-family: 'Courier New', Courier, monospace; font-size: 35px;">Available Vaccination Centers</h1>
        <h2 style="font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">CENTER</h2>

        <ul>
            {% for center in centers %}
            <li>
                <h3 style="font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; font-weight: bold; color:royalblue;">
                    {{center["center_details"]["name"]}}
                </h3>
                <table>
                    {% for key in center["center_details"] %}
                    <tr>
                        <th style="border: 1px solid black;"> {{ key }}: </th>
                        <td style="border: 1px solid black"> {{ center["center_details"][key] }} </td>
                    </tr>
                    {% endfor %}
                </table>

                <br>

                <h3 style="font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif; font-weight: bold; color:royalblue;">
                    Vaccination Sessions
                </h3>

                <table>
                    {% for sessions in center["sessions"] %} {% for key in sessions %}
                    <tr>
                        <th style="border: 1px solid black;"> {{ key }}: </th>
                        <td style="border: 1px solid black"> {{ sessions[key] }} </td>
                    </tr>
                    {% endfor %}

                    <br>

                    {% endfor %}
                </table>
            </li>
            {% endfor %}
        </ul>
    </div>

</body>


</html>
"""


def mail_notification(**kwargs):
    recipient_address = kwargs["email"]
    subject = "Available Vaccination Centers"

    with open('centers.json', 'r') as openfile:
        available_centers = json.load(openfile)
        template_value = Template(template_html)
        HTML_content = template_value.render(centers=available_centers)
        send_email(recipient_address, subject, HTML_content)