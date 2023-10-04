import gspread
from google.oauth2.service_account import Credentials
import pyinputplus as pyip
import sys
from datetime import date

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

    name = pyip.inputRegex(
        r"^([A-Za-z]+\s[A-Za-z]+)$", prompt="Client's Full Name: \n"
    ).title()
    email = pyip.inputEmail("Email address: \n")
    age = pyip.inputInt("Age: \n", min=18)
    print("Goal distance: \n")
    distance = pyip.inputMenu(
        ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
    )
    current_pb = str(
        pyip.inputTime(f"Current PB for {distance} to nearest minute as hh:mm : \n")
    )
    next_race = pyip.inputDate(f"Date of next {distance} race as mm/dd/yyyy: \n")
    goal_time = str(
        pyip.inputTime(
            f"Goal time for next {distance} race to nearest minute as hh:mm : \n"
        )
    )

    client_data = [name, email, age, distance, current_pb, str(next_race), goal_time]
    return client_data


def calculate_days_until_next_race(data):
    """
    Calculates a countdown for how many days left until the client's race day
    """
    next_race = data[5]
    next_race_date = date.fromisoformat(next_race)
    today = date.today()
    days_til_race = abs(next_race_date - today)
    data.append(days_til_race.days)
    return data


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
    Displays the client's data retreived using their email address.
    Then offers the user options to edit the client's data.
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
        new_name = pyip.inputRegex(
            r"^([A-Za-z]+\s[A-Za-z]+)$", prompt="Update client's Full Name: \n"
        ).title()
        running_worksheet.update_cell((data + 1), 1, new_name)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Email":
        new_email = pyip.inputEmail("Update email address: \n")
        running_worksheet.update_cell((data + 1), 2, new_email)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Age":
        new_age = pyip.inputInt("Update age: \n", min=18)
        running_worksheet.update_cell((data + 1), 3, new_age)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Goal distance":
        print(
            "You will need to update the current PB for this distance and the goal time too \n"
        )
        print("New goal distance: \n")
        new_goal_distance = pyip.inputMenu(
            ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
        )
        new_pb = str(
            pyip.inputTime("PB for this distance to nearest minute as hh:mm : \n")
        )
        new_goal_time = str(
            pyip.inputTime(
                "Goal time for the next race of this distance to nearest minute as hh:mm : \n"
            )
        )
        running_worksheet.update_cell((data + 1), 4, new_goal_distance)
        running_worksheet.update_cell((data + 1), 5, new_pb)
        running_worksheet.update_cell((data + 1), 7, new_goal_time)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "New PB":
        new_pb = str(pyip.inputTime("New PB to nearest minute as hh:mm : \n"))
        running_worksheet.update_cell((data + 1), 5, new_pb)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Next race date":
        new_next_race_date = str(pyip.inputDate("Date of next race as mm/dd/yyyy: \n"))
        running_worksheet.update_cell((data + 1), 6, new_next_race_date)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Goal Time":
        new_goal_time = str(
            pyip.inputTime("Goal time for next race to nearest minute as hh:mm : \n")
        )
        running_worksheet.update_cell((data + 1), 7, new_goal_time)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))


def delete_client_data(data):
    """
    Displays a client's data. Gives option to delete the client's data.
    If answer is yes, deletes the client's data from the googlesheet database.
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
            "Edit a client",
            "Delete a client",
            "Exit",
        ],
        numbered=True,
    )
    print("\n")
    if actions == "Add a client":
        new_client = new_client_data()
        new_client_with_days = calculate_days_until_next_race(new_client)
        add_new_client_to_worksheet(new_client_with_days)
        print(new_client)
        print("\n")
        client_list_menu()
    elif actions == "Display a client":
        searched_client_index = search_client_email()
        if searched_client_index:
            display_client_data(searched_client_index)
            print("\n")
            client_list_menu()
        else:
            print("\n")
            client_list_menu()
    elif actions == "Edit a client":
        searched_client_index = search_client_email()
        if searched_client_index:
            edit_client_data(searched_client_index)
            print("\n")
            client_list_menu()
        else:
            print("\n")
            client_list_menu()
    elif actions == "Delete a client":
        searched_client_index = search_client_email()
        if searched_client_index:
            delete_client_data(searched_client_index)
            print("\n")
            client_list_menu()
        else:
            print("\n")
            client_list_menu()
    elif actions == "Exit":
        print("See you next time!")
        sys.exit()


# def clear_screen(): os.system("cls")


def main():
    """
    Runs function to display list of actions in the program
    """
    client_list_menu()


print("Welcome to your Running Client List Data Automation\n")
main()
