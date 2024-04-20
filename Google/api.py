import os.path

import gspread
from google.oauth2.service_account import Credentials
from google.oauth2.credentials import Credentials as UserCredentials


CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")


def get_client():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    credentials = Credentials.from_service_account_file(
        CREDENTIALS_PATH, scopes=scopes)

    client = gspread.authorize(credentials)

    return client


def get_user_client(user):
    token = user.socialaccount_set.get(provider="google").socialtoken_set.get().token
    refresh_token = user.socialaccount_set.get(provider="google").socialtoken_set.get().token_secret

    credentials = UserCredentials(
        token=token,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    client = gspread.authorize(credentials)

    return client


def write_to_sheet(sheet_name, range_name, data, user=None):
    client = get_user_client(user) if user else get_client()

    client.open("New Spreadsheet").worksheet(sheet_name).update(range_name=range_name, data=data)


def read_from_sheet(range_name):
    client = get_client()

    values = client.open("New Spreadsheet").sheet1.get(range_name)

    return values
