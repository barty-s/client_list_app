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


def add_new_client_to_worksheet(data):
    """
    Adds the new client's information to running client list spreadsheet
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
        return client_index

    except ValueError:
        print("Client does not exist")


def display_client_data(data):
    """Displays the client data retreived using the client's email address"""
    print(running_worksheet.row_values((data + 1)))


def delete_client_data(data):
    """
    Displays a client's data. Gives option to delete the client's data. If answer is yes, deletes the client's data from the googlesheet database
    """
    display_client_data(data)
    delete_query = pyip.inputYesNo(
        "Are you sure you want to delete this client? - enter y/n\n"
    )

    if delete_query == "yes":
        running_worksheet.delete_rows((data + 1))
        print("Client successfully deleted")
    else:
        print("Client data not deleted")


def client_list_menu():
    print("What you like to do? Type a number from the list below:\n")
    actions = pyip.inputMenu(
        ["Add a client", "Display a client", "Delete a client"],
        numbered=True,
    )

    if actions == "Add a client":
        new_client = new_client_data()
        add_new_client_to_worksheet(new_client)
        print(new_client)
    elif actions == "Display a client":
        searched_client_index = search_client_email()
        display_client_data(searched_client_index)
    elif actions == "Delete a client":
        searched_client_index = search_client_email()
        delete_client_data(searched_client_index)


def main():
    """
    Runs all functions in the program
    """
    # new_client = new_client_data()
    # add_new_client_to_worksheet(new_client)
    # print(new_client)
    # searched_client_index = search_client_email()
    # display_client_data(searched_client_index)
    # delete_client_data(searched_client_index)
    client_list_menu()


print("Welcome to your Running Client List Data Automation\n")
main()
