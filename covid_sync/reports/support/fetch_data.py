import os

import pandas as pd

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
file_path = os.path.dirname(os.path.realpath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(file_path, "key.json")

# SERVICE_ACCOUNT_FILE = 'support\key.json'
# print(SERVICE_ACCOUNT_FILE)

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1EbJDUvYzy2tmeVCh8sfMSI7jJQYsEBYFvpLEsacQVYw'


def create_dataframe(values):
    column_names = values[0]
    values.remove(column_names)

    stats = pd.DataFrame(values, columns=column_names)

    del stats['Timestamp']

    return stats.to_html()


def fetch_data():
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="sheet1").execute()
    values = result.get('values', [])

    return create_dataframe(values)