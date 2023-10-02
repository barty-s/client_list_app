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

# data = running_worksheet.get_all_values() - use this to retrieve client with email address?

client_data = []


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
    current_pb = str(pyip.inputTime("Current PB to nearest minute as hh:mm : "))
    next_race = str(pyip.inputDate("Date of next race as mm/dd/yyyy: "))
    goal_time = str(
        pyip.inputTime("Goal time for next race to nearest minute as hh:mm : ")
    )

    client_data = [name, email, age, distance, current_pb, next_race, goal_time]
    return client_data


def update_running_worksheet(data):
    """
    Add the new client's information to running client list spreadsheet
    """
    print("Adding client to database...\n")
    running_worksheet.append_row(data)
    print("Client successfully added\n")


def search_client_email():
    """
    Searches for client using their email address
    """
    try:
        client_email = pyip.inputEmail("Search by client's email address: ")
        email_list = running_worksheet.col_values(2)
        client_index = email_list.index(client_email)
        print(running_worksheet.row_values((client_index + 1)))
    except ValueError:
        print("Client does not exist")


def delete_client_data():
    try:
        client_email = pyip.inputEmail("Search by client's email address: ")
        email_list = running_worksheet.col_values(2)
        client_index = email_list.index(client_email)

    except ValueError:
        print("Client does not exist")

    delete_query = pyip.inputYesNo("Are you sure you want to delete this client?")
    if delete_query:
        running_worksheet.delete_rows((client_index + 1))
        print("Client successfully deleted")


def main():
    """
    Runs all functions in the program
    """
    # new_client = new_client_data()
    # update_running_worksheet(new_client)
    # print(new_client)
    # search_client_email()
    delete_client_data()


print("Welcome to your Running Client List Data Automation\n")
main()
