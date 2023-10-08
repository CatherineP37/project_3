import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDITS = Credentials.from_service_account_file('credits.json')
SCOPED_CREDITS = CREDITS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDITS)
SHEET = GSPREAD_CLIENT.open('Appointments')

appointments = SHEET.worksheet('Appointments')

data = appointments.get_all_values()

print(data)

