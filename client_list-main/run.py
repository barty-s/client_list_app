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

running = SHEET.worksheet("running")

data = running.get_all_values()


def new_client_data():
    """
    User adds data about their new client
    """
    print("Let's add a new client")

    name = input("Name: ")
    email = pyip.inputEmail("Email address: ")
    age = pyip.inputInt("Age: ", min=18)
    print("Goal distance: ")
    distance = pyip.inputMenu(
        ["5km", "10km", "half-marathon", "marathon"], numbered=True
    )
    current_pb = pyip.inputTime("Current PB to nearest minute as 00:00 : ")
    next_race = pyip.inputDate("Date of next race as mm/dd/yyyy: ")
    goal_time = pyip.inputTime("Goal time for next race to nearest minute as 00:00 : ")

    print(
        f"New Client: Name - {name}, Email - {email}, Age - {age}  Race distance - {distance} Current PB - {current_pb} Next race on {next_race} with a goal time of {goal_time}"
    )


new_client_data()
# print(data)
