import gspread
from google.oauth2.service_account import Credentials
import pyinputplus as pyip
import sys

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

    name = input("Name: \n")
    email = pyip.inputEmail("Email address: \n")
    age = pyip.inputInt("Age: \n", min=18)
    print("Goal distance: \n")
    distance = pyip.inputMenu(
        ["5km", "10km", "half-marathon", "marathon" "\n"], numbered=True
    )
    current_pb = str(pyip.inputTime("Current PB to nearest minute as hh:mm : \n"))
    next_race = str(pyip.inputDate("Date of next race as mm/dd/yyyy: \n"))
    goal_time = str(
        pyip.inputTime("Goal time for next race to nearest minute as hh:mm : \n")
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
        client_email = pyip.inputEmail("Search by client's email address: \n")
        email_list = running_worksheet.col_values(2)
        client_index = email_list.index(client_email)
        return client_index

    except ValueError:
        print("Client does not exist")


def display_client_data(data):
    """Displays the client data retreived using the client's email address"""
    print(running_worksheet.row_values((data + 1)))


def edit_client_data(data):
    """
    Displays the client data retreived using the client's email address and offers the user options to edit the client's data
    """
    display_client_data(data)
    print("\n")
    print("What would you like to edit?\n")
    edit_actions = pyip.inputMenu(
        [
            "Name",
            "Email",
            "Age",
            "Goal distance",
            "Current PB",
            "Next race date",
            "Goal time",
        ],
        numbered=True,
    )

    if edit_actions == "Name":
        new_name = input("Name: \n")
        running_worksheet.update_cell((data + 1), 1, new_name)
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
    """
    Displays a list of actions for the user to choose from i.e add, display, delete client or exit program.
    The main menu is displayed again after each action is completed.
    """
    print("What you like to do? Type a number from the list below:\n")
    actions = pyip.inputMenu(
        [
            "Add a client",
            "Display a client",
            "Delete a client",
            "Edit a client",
            "Exit" "\n",
        ],
        numbered=True,
    )

    if actions == "Add a client":
        new_client = new_client_data()
        add_new_client_to_worksheet(new_client)
        print(new_client)
        client_list_menu()
    elif actions == "Display a client":
        searched_client_index = search_client_email()
        display_client_data(searched_client_index)
        client_list_menu()
    elif actions == "Delete a client":
        searched_client_index = search_client_email()
        delete_client_data(searched_client_index)
        client_list_menu()
    elif actions == "Edit a client":
        searched_client_index = search_client_email()
        edit_client_data(searched_client_index)
    elif actions == "Exit":
        print("See you next time")
        sys.exit()


# def clear_screen(): os.system("cls")


def main():
    """
    Runs function to display list of actions in the program
    """
    client_list_menu()


print("Welcome to your Running Client List Data Automation\n")
main()
