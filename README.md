# Client List App

## Purpose of the Project

The purpose of this app is to allow a running trainer to access their list of clients.
The user, i.e. the trainer, can add new clients, view clients, edit clients' information and delete clients, as needed. There are also automated calculations done on the input data to determine the training needs of the client which will assist the trainer in making a training plan. It is assumed that a new client has previous running experience and is hiring this trainer to improve their running time, therefore all inputs must be completed.

- Live site: https://running-client-list-cbd69015c7bc.herokuapp.com/
- Googlesheets link: https://docs.google.com/spreadsheets/d/17M0THf5HOCmTCS_M8pkf5eGf52iwv_LcsSCPS_9-gNo/edit?usp=sharing

## User Stories

## Features

- Add in workflow to demonstrate the features

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

- CI run-through project - Code to access APIs and Google Sheets
- for contact book structure explanation https://www.geeksforgeeks.org/implementing-a-contacts-directory-in-python/
- https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response - for info on input validation
- PyInputPlus info and explanation - https://pyinputplus.readthedocs.io/en/latest/ , https://dev.to/dominickoech/input-validation-using-pyinputplus-module-in-python-455p, https://stackoverflow.com/questions/66494597/pyinputplus-allowregexes-keyword-allows-any-input
- Serialization for datetime (JSON) - https://www.youtube.com/watch?v=-2PrvZ420QM&t=405s (not used in the end)
- For explanation of index() method - https://www.programiz.com/python-programming/methods/list/index
- For explanation of googlesheets methods - https://www.python-engineer.com/posts/google-sheets-api/ , https://www.geeksforgeeks.org/using-google-sheets-as-database-in-python/
- datetime and date countdown explanation - https://www.dataquest.io/blog/python-datetime/, https://docs.python.org/3/library/datetime.html
- for help with date validation - https://stackoverflow.com/questions/64601493/time-cannot-be-set-in-the-past-condition-python
