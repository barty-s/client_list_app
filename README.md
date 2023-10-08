# Client List App

## Purpose of the Project

The purpose of this app is to allow a running trainer to access their list of clients.
The user, i.e. the trainer, can add new clients, view clients, edit clients' information and delete clients, as needed. There are also automated calculations done on the input data to determine the training needs of the client which will assist the trainer in making a training plan. It is assumed that a new client has previous running experience and is hiring this trainer to improve their running time, therefore all inputs must be completed.

- Live site: https://running-client-list-cbd69015c7bc.herokuapp.com/
- Googlesheets link: https://docs.google.com/spreadsheets/d/17M0THf5HOCmTCS_M8pkf5eGf52iwv_LcsSCPS_9-gNo/edit?usp=sharing

## User Stories

1. As a user, a running trainer, I want to be able to add my client's data and have the program give me outputs on how many days until the client's next race.
2. As a user, I want to be able to view my client's information on searching the spreadsheet with their email address.
3. As a user, I want to be able to edit any of the client's data.
4. As a user, I want to be able to delete a client from the client list if I need to.

## Features

<img src='/readme/workflow.png' >

As demonstated in the workflow image above, this app has 5 main features:

1. Add a client - the user can input their new client's data. The user will have to input:

- the client's full name
- a valid email address which doesn't already exist in the client list
- the client's age, with the minimum age being 18
- the race distance the client is training for
- the client's current Personal Best (PB) time for the race distance
- the date of the client's next race, in mm/dd/yyyy format and which must be a future date
- the time the client wants to complete this race in
  The data will be displayed once all the input sections have been correctly completed, and the user will be shown how many days there are until the client's next race.

2. Display a client - the user can search for an existing client and their data will be displayed. Originally, the client's last name was going to be used to search but during the development of the app I was advised to use the client's email, as that is a unique datum and will avoid issues if there exists multiple clients with the same last name.

3. Edit a client - the user can search for a client using their email address. If the client exists the user will be given the option to edit any of the inputs. If the user wants to edit the race distance, they will be asked to edit the client's PB and goal time too

4. Delete a client - the user can search for a client using their email address. The client's data will be displayed and the user will be asked if they are sure they want to delete the information and choose Y or N.

5. Exit - the user can exit the program

## Future Features

- to allow for clients with no previous running experience
- to create options for other sports such as cycling, swimming, weight-lifting depending on the trainer's area of expertise

## Technologies

- PyInputPlus module - for additional input validation
- google oauth - to access credentials in the creds.json file
- gspread - to link the googlesheets spreadsheet to the app actions
- sys module - to access the interpreter
- datetime - to format date and time inputs
- tabulate - to format data into tables

## Testing

## Deployment

## Credits

- https://www.lucidchart.com - to create the workflow image
- CI run-through project - code to access APIs and Google Sheets
- https://www.geeksforgeeks.org/implementing-a-contacts-directory-in-python/ - for contact book structure explanation
- https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response - for info on input validation
- https://pyinputplus.readthedocs.io/en/latest/ , https://dev.to/dominickoech/input-validation-using-pyinputplus-module-in-python-455p, https://stackoverflow.com/questions/66494597/pyinputplus-allowregexes-keyword-allows-any-input - PyInputPlus info and explanations
- https://www.youtube.com/watch?v=-2PrvZ420QM&t=405s - Serialization for datetime (JSON) - (not used in the end)
- https://www.programiz.com/python-programming/methods/list/index - For explanation of index() method -
- https://www.python-engineer.com/posts/google-sheets-api/ , https://www.geeksforgeeks.org/using-google-sheets-as-database-in-python/ - For explanation of googlesheets methods
- https://www.dataquest.io/blog/python-datetime/, https://docs.python.org/3/library/datetime.html -datetime and date countdown explanation
- https://stackoverflow.com/questions/64601493/time-cannot-be-set-in-the-past-condition-python - for help with date validation
