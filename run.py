""" Modules used in the program """
import sys
import os
from datetime import date, time, datetime
import time as t
import pyinputplus as pyip
from termcolor import colored as col
import spreadsheet


# Global variables list
running_worksheet = spreadsheet.SHEET.worksheet("running")
client_data = []
today = date.today()


def new_client_data():
    """
    User adds data about their new client
    """
    os.system("cls" if os.name == "nt" else "clear")
    print(col("Let's add a new client\n", "green"))

    name = pyip.inputRegex(
        r"^([A-Za-z]+\s[A-Za-z]+)$", prompt="Client's First and Last Name: \n"
    ).title()
    print("\n")
    client_email = pyip.inputEmail("Email address: \n")
    validated_email = validate_email(client_email)
    print("\n")
    age = pyip.inputInt("Age: \n", min=18, max=100)
    print("\n")
    print("Goal distance: \n")
    race_distance = pyip.inputMenu(
        ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
    )
    print("\n")
    print(f"Current PB for {race_distance} as hh:mm :")
    current_pb = validate_times(race_distance)
    print("\n")
    print(f"Goal time for next {race_distance} as hh:mm :")
    goal_time = validate_times(race_distance)
    print("\n")
    print(f"Date of next {race_distance} race:")
    print(col("Race date can't be after 12/31/2030", "cyan"))
    next_race = pyip.inputDate("(Please type as mm/dd/yyyy)\n")
    validated_next_race = validate_race_date(next_race)

    new_data = [
        name,
        validated_email,
        age,
        race_distance,
        str(current_pb),
        str(goal_time),
        str(validated_next_race),
    ]
    return new_data


def validate_email(email):
    """
    Checks database to see if a client already exists
    with the input email address. Warns user if a client
    already exists with that email.
    """
    email_list = running_worksheet.col_values(2)
    if email in email_list:
        print(col("A client already exists with this email \n", "red"))
        client_list_menu()
    else:
        return email


def validate_times(distance):
    """
    Depending on the distance of the client's race, asks the user to
    input the client's personal best and goal times.
    There are min and max time limits on each race distance
    using the world record times as min values
    and standard race limits as max values.
    """
    if distance == "5km":
        print(col("The max time for a 5km race is 00:59", "cyan"))
        hours = pyip.inputInt("hh: \n", min=0, max=0)
        if hours == 0:
            minutes = pyip.inputInt("mm: \n", min=12, max=59)
        else:
            minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time
    if distance == "10km":
        print(col("The max time for a 10km race is 01:59", "cyan"))
        hours = pyip.inputInt("hh: \n", min=0, max=1)
        if hours == 0:
            minutes = pyip.inputInt("mm: \n", min=26, max=59)
        else:
            minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time
    if distance == "Half-Marathon":
        print(col("The max time for a Half-Marathon race is 03:59", "cyan"))
        hours = pyip.inputInt("hh: \n", min=0, max=3)
        if hours == 0:
            minutes = pyip.inputInt("mm: \n", min=57, max=59)
        else:
            minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time
    if distance == "Marathon":
        print(col("The max time for a Marathon race is 06:59", "cyan"))
        hours = pyip.inputInt("hh: \n", min=2, max=6)
        minutes = pyip.inputInt("mm: \n", max=59)
        race_time = time(hours, minutes)
        return race_time


def validate_race_date(input_date):
    """
    Makes sure that the date entered by the user for the client's next race
    is in the future and before the limit of 01/01/2031
    """
    date_limit = date.fromisoformat("2031-01-01")

    while True:
        if today >= input_date:
            print(col("Race date must be in the future!", "red"))
            print(col("Please try again...", "red"))
            input_date = pyip.inputDate("Date of next race as mm/dd/yyyy: \n")
        elif input_date >= date_limit:
            print(col("The race date limit is 12/31/2030", "red"))
            input_date = pyip.inputDate("Date of next race as mm/dd/yyyy: \n")
        else:
            return input_date


def calculate_days_until_next_race(data):
    """
    Calculates a countdown for how many
    days are left until the client's next race
    """
    next_race = data[6]
    next_race_date = date.fromisoformat(next_race)
    days_til_race = abs(next_race_date - today)
    return days_til_race.days


def append_days_til_race(data, days):
    """
    Appends the days-until-the-next-race calculation to the client's data
    """
    data.append(days)
    return data


def calculate_pb(data):
    """
    Calculates the client's pb running pace
    """
    distance = data[3]
    pb_time = datetime.strptime(data[4], "%H:%M:%S")
    total_minutes = (pb_time.hour * 60) + pb_time.minute
    if distance == "5km":
        pb_pace = total_minutes / 5
    elif distance == "10km":
        pb_pace = total_minutes / 10
    elif distance == "Half-Marathon":
        pb_pace = total_minutes / 21.0975
    elif distance == "Marathon":
        pb_pace = total_minutes / 42.195
    seconds = pb_pace * 60
    m = int(seconds % 3600 / 60)
    s = int(seconds % 60)
    if s == 0:
        return f"{m}:00"
    return f"{m}:{s}"


def calculate_goal_pace(data):
    """
    Calculates the client's goal race pace
    """
    distance = data[3]
    goal_time = datetime.strptime(data[5], "%H:%M:%S")
    total_minutes = (goal_time.hour * 60) + goal_time.minute
    if distance == "5km":
        goal_pace = total_minutes / 5
    elif distance == "10km":
        goal_pace = total_minutes / 10
    elif distance == "Half-Marathon":
        goal_pace = total_minutes / 21.0975
    elif distance == "Marathon":
        goal_pace = total_minutes / 42.195
    seconds = goal_pace * 60
    m = int(seconds % 3600 / 60)
    s = int(seconds % 60)
    if s == 0:
        return f"{m}:00"
    return f"{m}:{s}"


def append_race_pace(data, pace):
    """
    Appends the client's running pace to their row of data
    """
    data.append(pace)
    return data


def add_new_client_to_worksheet(data):
    """
    Adds the new client's information to running client list spreadsheet
    """
    print(col("Adding client to database...\n", "yellow"))
    running_worksheet.append_row(data)
    t.sleep(1.5)
    print(col("Client successfully added!\n", "green"))
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")


def search_client_email():
    """
    Searches for client using their email address
    """
    os.system("cls" if os.name == "nt" else "clear")
    try:
        email = pyip.inputEmail(col("Search by email address:\n", "blue"))
        email_list = running_worksheet.col_values(2)
        client_index = email_list.index(email)
        return client_index

    except ValueError:
        print(col("Client does not exist", "red"))


def get_client_data(data):
    """
    Retreives client's data using their email
    address and updates the days til race countdown
    """
    retrieved_data = retrieve_row(data)
    updated_days = calculate_days_until_next_race(retrieved_data)
    update_wks_cell(data, 8, str(updated_days))
    updated_client = retrieve_row(data)
    return updated_client


def edit_client_data(data):
    """
    Displays the client's data retrieved using their email address.
    Then offers the user options to edit the client's data.
    """
    os.system("cls" if os.name == "nt" else "clear")
    update_client_data = get_client_data(data)
    view_client_data(update_client_data)
    print("\n")
    print(col("What would you like to edit?\n", "magenta"))
    edit_actions = pyip.inputMenu(
        [
            "Name",
            "Email",
            "Age",
            "Goal Distance",
            "Current PB",
            "Goal Time",
            "Next Race Date",
            "Return to Main Menu",
        ],
        numbered=True,
    )

    if edit_actions == "Name":
        edit_name(data)
    elif edit_actions == "Email":
        edit_email(data)
    elif edit_actions == "Age":
        edit_age(data)
    elif edit_actions == "Goal Distance":
        edit_gd(data)
    elif edit_actions == "Current PB":
        edit_current_pb(data)
    elif edit_actions == "Goal Time":
        edit_gt(data)
    elif edit_actions == "Next Race Date":
        edit_race_date(data)
    elif edit_actions == "Return to Main Menu":
        os.system("cls" if os.name == "nt" else "clear")
        client_list_menu()


def edit_name(data):
    """
    Edits the client's name in the database
    """
    new_name = pyip.inputRegex(
        r"^([A-Za-z]+\s[A-Za-z]+)$", prompt="Update Full Name: \n"
    ).title()
    update_wks_cell(data, 1, new_name)
    print(col("Client successfully updated \n", "green"))
    updated_client = retrieve_row(data)
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(updated_client)


def edit_email(data):
    """
    Edits the client's email in the database
    """
    new_email = pyip.inputEmail("Update email address: \n")
    validated_new_email = validate_email(new_email)
    update_wks_cell(data, 2, validated_new_email)
    print(col("Client successfully updated \n", "green"))
    updated_client = retrieve_row(data)
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(updated_client)


def edit_age(data):
    """
    Edits the client's age in the database
    """
    new_age = pyip.inputInt("Update age: \n", min=18, max=100)
    update_wks_cell(data, 3, new_age)
    print(col("Client successfully updated \n", "green"))
    updated_client = retrieve_row(data)
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(updated_client)


def edit_gd(data):
    """
    Edits the clients goal distance and corresponding
    current PB and goal time in the database
    """
    update_client_data = get_client_data(data)
    goal_distance = str(update_client_data[3])
    print(col("You will need to update the current PB for", "cyan"))
    print(col("this distance and the goal time too \n", "cyan"))
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    print("New goal distance: \n")
    new_goal_distance = pyip.inputMenu(
        ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
    )
    while new_goal_distance == goal_distance:
        print(col("Please select a new distance\n", "red"))
        new_goal_distance = pyip.inputMenu(
            ["5km", "10km", "Half-Marathon", "Marathon"], numbered=True
        )
    print(f"Enter the client's PB for {new_goal_distance}")
    new_pb = validate_times(new_goal_distance)
    print(f"Enter the client's goal time for {new_goal_distance}")
    new_goal_time = validate_times(new_goal_distance)
    update_wks_cell(data, 4, new_goal_distance)
    update_wks_cell(data, 5, str(new_pb))
    update_wks_cell(data, 6, str(new_goal_time))
    updated_client = retrieve_row(data)
    new_pb_pace = calculate_pb(updated_client)
    new_goal_pace = calculate_goal_pace(updated_client)
    update_wks_cell(data, 9, str(new_pb_pace))
    update_wks_cell(data, 10, str(new_goal_pace))
    print(col("Client successfully updated \n", "green"))
    fully_updated_client = retrieve_row(data)
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(fully_updated_client)


def edit_current_pb(data):
    """
    Edits the client's current PB
    """
    update_client_data = get_client_data(data)
    goal_distance = str(update_client_data[3])
    print(f"Enter the client's updated PB for {goal_distance}")
    new_pb = validate_times(goal_distance)
    update_wks_cell(data, 5, str(new_pb))
    updated_pb = retrieve_row(data)
    new_pb_pace = calculate_pb(updated_pb)
    update_wks_cell(data, 9, str(new_pb_pace))
    updated_client = retrieve_row(data)
    print(col("Client successfully updated \n", "green"))
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(updated_client)


def edit_gt(data):
    """Edits the client's goal time in the database"""
    update_client_data = get_client_data(data)
    goal_distance = str(update_client_data[3])
    print(f"Enter the client's updated goal time for {goal_distance}")
    new_goal_time = validate_times(goal_distance)
    update_wks_cell(data, 6, str(new_goal_time))
    updated_goal_time = retrieve_row(data)
    new_goal_pace = calculate_goal_pace(updated_goal_time)
    update_wks_cell(data, 10, str(new_goal_pace))
    updated_client = retrieve_row(data)
    print(col("Client successfully updated \n", "green"))
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(updated_client)


def edit_race_date(data):
    """Edits the client's race date in the database"""
    new_race_date = pyip.inputDate("Date of next race as mm/dd/yyyy:\n")
    validated_date = validate_race_date(new_race_date)
    update_wks_cell(data, 7, str(validated_date))
    updated_client = retrieve_row(data)
    update_client_days = calculate_days_until_next_race(updated_client)
    update_wks_cell(data, 8, str(update_client_days))
    print(col("Client successfully updated \n", "green"))
    updated_client = retrieve_row(data)
    t.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")
    view_client_data(updated_client)


def update_wks_cell(data, index, info):
    """
    Updates a given cell in the googlesheets database
    """
    running_worksheet.update_cell((data + 1), index, info)


def retrieve_row(data):
    """
    Retrieves the row of data for a given client
    """
    retrieved_data = running_worksheet.row_values((data + 1))
    return retrieved_data


def delete_client_data(data):
    """
    Displays a client's data. Gives option to delete the client's data.
    If answer is yes, deletes the client's data from the googlesheet database.
    """
    os.system("cls" if os.name == "nt" else "clear")
    search_client_data = get_client_data(data)
    view_client_data(search_client_data)
    print("\n")
    print(col("Are you sure you want to delete this client?", "magenta"))
    delete_query = pyip.inputYesNo(col("Please type y or n\n", "magenta"))

    if delete_query == "yes":
        running_worksheet.delete_rows((data + 1))
        t.sleep(1.5)
        print(col("Client successfully deleted \n", "green"))
        t.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")
    else:
        t.sleep(1.5)
        print(col("Client data not deleted \n", "yellow"))
        t.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")


def view_client_data(data):
    """
    Displays client data in an easily readable format
    """
    print(col("CLIENT DATA", "green"))
    print(f"Name: {data[0]}")
    print(f"Email: {data[1]}")
    print(f"Age: {data[2]}")
    print(f"Race Distance: {data[3]}")
    print(f"PB: {data[4]}")
    print(f"Goal time: {data[5]}")
    print(f"Next Race: {data[6]}")
    print(f"Days until next race: {data[7]}")
    print(f"Current Pace: {data[8]} mins/km")
    print(f"Goal Pace: {data[9]} mins/km")


def client_list_menu():
    """
    Displays a list of actions for the user to choose from.
    The user can add, display, edit, delete a client or exit program.
    The main menu is displayed again after each action is completed.
    """
    print(col("What would you like to do?", "magenta"))
    print(col("Type a number from the list below:", "magenta"))
    print("\n")
    actions = pyip.inputMenu(
        [
            "Add a client",
            "View a client",
            "Edit a client",
            "Delete a client",
            "Exit",
        ],
        numbered=True,
    )
    print("\n")
    if actions == "Add a client":
        add_client()
    elif actions == "View a client":
        view_client()
    elif actions == "Edit a client":
        edit_client()
    elif actions == "Delete a client":
        delete_client()
    elif actions == "Exit":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n")
        print(col("See you next time! \n", "cyan"))
        sys.exit()


def add_client():
    """
    Calls the functions to allow user
    to add a new client to the database
    """
    new_client = new_client_data()
    days_countdown = calculate_days_until_next_race(new_client)
    client_appended_days = append_days_til_race(new_client, days_countdown)
    client_pb = calculate_pb(new_client)
    client_appended_pb = append_race_pace(client_appended_days, client_pb)
    client_goal_pace = calculate_goal_pace(new_client)
    client_appended_race_pace = append_race_pace(client_appended_pb, client_goal_pace)
    add_new_client_to_worksheet(client_appended_race_pace)
    view_client_data(new_client)
    print("\n")
    client_list_menu()


def view_client():
    """
    Calls the functions to display the client's data to the user
    """
    searched_client_index = search_client_email()
    if searched_client_index:
        searched_client_data = get_client_data(searched_client_index)
        print("\n")
        view_client_data(searched_client_data)
        print("\n")
        client_list_menu()
    else:
        print("\n")
        client_list_menu()


def edit_client():
    """ "
    Calls the functions to allow user to edit client's data
    """
    searched_client_index = search_client_email()
    if searched_client_index:
        print("\n")
        edit_client_data(searched_client_index)
        print("\n")
        client_list_menu()
    else:
        print("\n")
        client_list_menu()


def delete_client():
    """
    Calls the functions to allow user to delete
    the selected client's data from the database
    """
    searched_client_index = search_client_email()
    if searched_client_index:
        delete_client_data(searched_client_index)
        print("\n")
        client_list_menu()
    else:
        print("\n")
        client_list_menu()


def main():
    """
    Runs function to display list of actions in the program
    """
    client_list_menu()


print("\n")
print("Welcome to the Running Client List Data Automation App\n")
main()
