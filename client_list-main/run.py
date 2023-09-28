import gspread
from google.oauth2.service_account import Credentials
import pyinputplus as pyip

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("client_list")

running_worksheet = SHEET.worksheet("running")

data = running_worksheet.get_all_values()


def new_client_data():
    """
    User adds data about their new client
    """
    print("Let's add a new client\n")

    name = input("Name: ")
    email = pyip.inputEmail("Email address: ")
    age = pyip.inputInt("Age: ", min=18)
    print("Goal distance: ")
    distance = pyip.inputMenu(
        ["5km", "10km", "half-marathon", "marathon"], numbered=True
    )
    current_pb = input("Current PB to nearest minute as hh:mm : ")
    # next_race = pyip.inputDate("Date of next race as mm/dd/yyyy: ")
    # goal_time = pyip.inputTime("Goal time for next race to nearest minute as hh:mm : ")

    client_data = [name, email, age, distance, current_pb]
    return client_data


def update_running_worksheet(data):
    """
    Add the new client's information to running client list spreadsheet
    """
    print("Adding client to database...\n")
    running_worksheet.append_row(data)
    print("Client successfully added\n")


new_client = new_client_data()
update_running_worksheet(new_client)
print(new_client)
