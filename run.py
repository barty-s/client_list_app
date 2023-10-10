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
    return days_til_race.days


def append_days_til_race(data, days):
    """
    Append the days until the next race calculation to the client's data
    """
    data.append(days)
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
    return running_worksheet.row_values((data + 1))


def edit_client_data(data):
    """
    Displays the client's data retreived using their email address.
    Then offers the user options to edit the client's data.
    """
    client_data = display_client_data(data)
    goal_distance = str(client_data[3])
    print("\n")
    print("What would you like to edit?\n")
    edit_actions = pyip.inputMenu(
        [
            "Name",
            "Email",
            "Age",
            "Goal Distance",
            "Current PB",
            "Goal Time",
            "Next Race Date",
            "Return to Main menu",
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
        validated_new_email = validate_email(new_email)
        running_worksheet.update_cell((data + 1), 2, validated_new_email)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Age":
        new_age = pyip.inputInt("Update age: \n", min=18, max=100)
        running_worksheet.update_cell((data + 1), 3, new_age)
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Goal Distance":
        print(
            "You will need to update the current PB for this distance and the goal time too \n"
        )
        print("New goal distance: \n")
        new_goal_distance = pyip.inputMenu(
            ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
        )
        print(f"Enter the client's PB for {new_goal_distance}")
        new_pb = validate_times(new_goal_distance)
        print(f"Enter the client's goal time for {new_goal_distance}")
        new_goal_time = validate_times(new_goal_distance)
        validated_new_goal_time = validate_goal_time(new_goal_time, new_goal_distance)
        running_worksheet.update_cell((data + 1), 4, new_goal_distance)
        running_worksheet.update_cell((data + 1), 5, str(new_pb))
        running_worksheet.update_cell((data + 1), 6, str(validated_new_goal_time))
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Current PB":
        print(f"Enter the client's updated PB for {goal_distance}")
        new_pb = validate_times(goal_distance)
        running_worksheet.update_cell((data + 1), 5, str(new_pb))
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Goal Time":
        print(f"Enter the cliet's updated goal time for {goal_distance}")
        new_goal_time = validate_times(goal_distance)
        validated_new_goal_time = validate_goal_time(new_goal_time, goal_distance)
        running_worksheet.update_cell((data + 1), 6, str(validated_new_goal_time))
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Next Race Date":
        new_next_race_date = pyip.inputDate("Date of next race as mm/dd/yyyy: \n")
        validated_new_next_race_date = validate_race_date(new_next_race_date)
        running_worksheet.update_cell((data + 1), 7, str(validated_new_next_race_date))
        updated_client = running_worksheet.row_values((data + 1))
        update_client_days = calculate_days_until_next_race(updated_client)
        running_worksheet.update_cell((data + 1), 8, str(update_client_days))
        print("Client successfully updated")
        print(running_worksheet.row_values((data + 1)))
    elif edit_actions == "Return to Main Menu":
        client_list_menu()


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
        days_countdown = calculate_days_until_next_race(new_client)
        client_appended_with_days = append_days_til_race(new_client, days_countdown)
        add_new_client_to_worksheet(client_appended_with_days)
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
