import gspread
from google.oauth2.service_account import Credentials
import pyinputplus as pyip
import sys
from datetime import date, time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("client_list")

# Global variables list
running_worksheet = SHEET.worksheet("running")
client_data = []
today = date.today()


def new_client_data():
    """
    User adds data about their new client
    """
    print("Let's add a new client\n")

    name = pyip.inputRegex(
        r"^([A-Za-z]+\s[A-Za-z]+)$", prompt="Client's First and Last Name: \n"
    ).title()
    client_email = pyip.inputEmail("Email address: \n")
    validated_email = validate_email(client_email)
    age = pyip.inputInt("Age: \n", min=18, max=100)
    print("Goal distance: \n")
    race_distance = pyip.inputMenu(
        ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
    )
    print(f"Current PB for {race_distance} to nearest minute as hh:mm :")
    current_pb = validate_times(race_distance)
    print(f"Goal time for next {race_distance} race to nearest minute as hh:mm :")
    goal_time = validate_times(race_distance)
    validated_goal_time = validate_goal_time(goal_time, race_distance)
    next_race = pyip.inputDate(f"Date of next {race_distance} race as mm/dd/yyyy: \n")
    validated_next_race = validate_race_date(next_race)

    client_data = [
        name,
        validated_email,
        age,
        race_distance,
        str(current_pb),
        str(validated_goal_time),
        str(validated_next_race),
    ]
    return client_data


def validate_email(email):
    """
    Checks database to see if a client already exists with the input email address and then warns user
    """
    email_list = running_worksheet.col_values(2)
    if email in email_list:
        print("A client already exists with this email")
        print("\n")
        client_list_menu()
    else:
        return email


def validate_times(distance):
    """
    Depending on the distance of the client's race, asks the user
    input the client's personal best and goal times, with max time limits on each race distance
    """
    if distance == "5km":
        print("The max time for a 5km race is 01:59")
        hours = pyip.inputInt("hh: \n", max=1)
        minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time
    elif distance == "10km":
        print("The max time for a 10km race is 02:59")
        hours = pyip.inputInt("hh: \n", max=2)
        minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time
    elif distance == "Half-Marathon":
        print("The max time for a Half-Marathon race is 03:59")
        hours = pyip.inputInt("hh: \n", max=3)
        minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time
    elif distance == "Marathon":
        print("The max time for a Marathon race is 07:59")
        hours = pyip.inputInt("hh: \n", max=7)
        minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time


def validate_goal_time(time, distance):
    """
    Ensures user cannot input a time of 00:00 for the race goal time
    """
    valid_goal_time = str(time)
    while True:
        if valid_goal_time == "00:00:00":
            print("Please enter a valid goal time")
            valid_goal_time = validate_times(distance)
        else:
            return valid_goal_time


def validate_race_date(date):
    """
    Makes sure that the date entered by the user for the client's next race
    is in the future and before the limit of 12/31/2030
    """
    date_limit = date.fromisoformat("2031-01-01")

    while True:
        if today >= date:
            print("Race date must be in the future! Please try again...")
            date = pyip.inputDate(f"Date of next race as mm/dd/yyyy: \n")
        elif date >= date_limit:
            print("The race date can't be later than 12/31/2030")
            date = pyip.inputDate(f"Date of next race as mm/dd/yyyy: \n")
        else:
            return date


def calculate_days_until_next_race(data):
    """
    Calculates a countdown for how many days are left until the client's race day
    """
    next_race = data[6]
    next_race_date = date.fromisoformat(next_race)
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
        new_age = pyip.inputInt("Update age: \n", min=18, max=100)
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
