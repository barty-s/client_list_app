import gspread
from google.oauth2.service_account import Credentials

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
    User adds all the data about their new client
    """
    print("Let's add a new client")

    name = input("Full name: ")
    email = input("Email address: ")
    while True:
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Data not valid")
            continue
        else:
            break
    if age < 18:
        print("This client is too young to train")

    distance = input("Goal distance: ")
    current_pb = input("Current PB: ")
    next_race = input("Date of next race: ")
    goal_time = input("Goal time for next race: ")

    print(
        f"New Client: Name - {name}, Email - {email}, Age - {age}  Race distance - {distance} Current PB - {current_pb} Next race on {next_race} with a goal time of {goal_time}"
    )


new_client_data()
# print(data)
