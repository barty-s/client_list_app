# Client List App

## Purpose of the Project

The purpose of this app is to allow a running trainer to access their list of clients.
The user, i.e. the trainer, can add new clients, view clients, edit clients' information and delete clients, as needed. There are also automated calculations done on the input data to determine the training needs of the client which will assist the trainer in making a training plan. It is assumed that a new client has previous running experience and is hiring this trainer to improve their running time, therefore all inputs must be completed.

- Live site: https://running-client-list-cbd69015c7bc.herokuapp.com/
- Googlesheets link: https://docs.google.com/spreadsheets/d/17M0THf5HOCmTCS_M8pkf5eGf52iwv_LcsSCPS_9-gNo/edit?usp=sharing

## User Stories

1. As a user, a running trainer, I want to be able to add my client's data and have the program give me outputs on how many days until the client's next race and what their current and goal race paces are.
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
  The data will be displayed once all the input sections have been correctly completed, and the user will be shown how many days there are until the client's next race as well as the client's current race pace and their goal race pace.

2. Display a client - the user can search for an existing client and their data will be displayed. Originally, the client's last name was going to be used to search but during the development of the app I was advised to use the client's email, as that is a unique datum and will avoid data retrieval issues if multiple clients with the same last name exist. Before the client is displayed, the up-to-date number of days until the race will be calculated and the client's data will be updated.

3. Edit a client - the user can search for a client using their email address. If the client exists the user will be given the option to edit any of the inputs. If the user wants to edit the race distance, they will be asked to edit the client's PB and goal time too. The current race pace and goal race pace will be updated accordingly. If the race date is changed, the new number of days until the race will be calculated and displayed.

4. Delete a client - the user can search for a client using their email address. The client's data will be displayed and the user will be asked if they are sure they want to delete the information and choose Y or N.

5. Exit - the user can exit the program

## Future Features

- I would like to allow for clients with no previous running experience to be added to the client list and develop the automated calculations to accomodate this feature.
- I would to create input and automated calculations options for other sports such as cycling, swimming, weight-lifting etc depending on the trainer's area of expertise and their clients' needs.
- I would like to improve the pb and goal time inputs to include ss to make their pace times more accurate

## Technologies

### Lanugages

- Python was solely used to create this app

### Programs

- Git - version control
- VSCode - as the program editor
- Black - Python auto formatter installed in VSCode
- GitHub Desktop - to commit and push changes in the app's code
- GitHub - to store the files in a repository and to link to Heroku
- Heroku - to host the app in a mock terminal
- Code Institutes Pep8 Checker - to test and validate the python code
- Lucid Chart - to create a flow chart of the actions available in the app
- Heroku - to deploy the app

### Modules

- PyInputPlus module - For additional input validation. I came across this module while I was researching how to validate email inputs. It has many built-in features that add automatic validation to emails, integers, strings, dates, times - all of which I made use of in this app.
- gspread - A Python API for Google Sheets which is used to access and update data stored in the 'running' sheet in the spread sheet 'client_list'.
- google.oauth2.service_account - To import the Credentials Class which then uses the creds.json file.
- sys module - To access the interpreter.
- datetime - To format date and time inputs, and to get the current date which is used in the countdown function.
- os - To clear the terminal screen after the user selects an action. This allows for better UX by displaying the data relevant to the action and avoid excessive scrolling.
- termcolor - To add color to various print statements to improve UX.
- time - To use the sleep() function so as to improve UX and slow down the speed of the messages being displayed.

## Testing

### Code Validation

- CI Python Linter https://pep8ci.herokuapp.com/

### Test Cases (user based with screenshots)

1. Main Menu - the app opens with a welcome message and asks the user to choose an action from the list.

### Fixed Bugs

- Next Race Date validation - Originally I had an if/else statement and that only checked once if the user had input a correct date, that is the user could first input an invalid date, be prompted to input a correct date, then input an invalid date again, and that would be accepted. So I changed it for a while loop to keep asking until the date fits within the limits.
- Edit Race Date - to ensure the countdown days until the next race was also updated, I realised I needed a new function and to separate the update countdown and the append functions. This was useful as I was then able to use the update countdown function in the display client option - the countdown days will be accurate to the day it is viewed.
- Enforce a minimum on the PB and Goal times - The user was able to input 00:01 for 5km/10km which doesn't make sense and produces strange race paces. So I decided to set a minimum/maximum limit for each race. The minimum time is the current world record for each race distance and the maximum time is the standard limit participants have to complete the race in. Normally, in organised races, there is a bus that follows the race pack and if there are people who are running too slowly, they are picked up by the bus so that the streets aren't blocked to other users for too long.

## Deployment

### To Deploy on Heroku

1. Use Code Institute's Python Essentials Template.
2. Create a new repository and write the program code.
3. Creat a requirements.txt file and add '\n' to the end of each input to accommodate the bug on Heroku.
4. Create a Heroku student account.
5. Log in and select create a new app.
6. Create an app name and region.
7. Select the deployment method to connect to the repository via GitHub, then search and connect the app repo.
8. Enable automatic deployment and select the main branch, or alternatively select manual deployment
9. In the settings tab select 'config vars' and copy/paste in the creds.json file. And also, 'PORT' with value 8000.
10. Add the buildpacks in this order: 1 - Python, 2 - Node.js
11. Finally, deploy the app

### To Fork the Repository

1. In the GitHub repository, click on the 'Fork' button
2. Edit the repository name and description
3. Click the green 'Create Fork' button

### To Clone The Repository

1. Navigate to the GitHub repository
2. Click the green 'Code' button
3. Select if you would prefer to clone using HTTPS, SSH, or Github CLI
4. Click the copy button to copy the URL to your clipboard
5. Open Git Bash and change the current working directory to the cloned directory
6. Type 'git clone' and paste the URL from the clipboard - press Enter to create your local clone.

## Credits

- To create the workflow image - https://www.lucidchart.com
- CI run-through project - code to access APIs and Google Sheets
- For an explanation of the structure of a contact book - https://www.geeksforgeeks.org/implementing-a-contacts-directory-in-python/
- For info on input validation - https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
- PyInputPlus info and explanations - https://pyinputplus.readthedocs.io/en/latest/ , https://dev.to/dominickoech/input-validation-using-pyinputplus-module-in-python-455p, https://stackoverflow.com/questions/66494597/pyinputplus-allowregexes-keyword-allows-any-input
- For an explanation of index() method - https://www.programiz.com/python-programming/methods/list/index
- For an explanation of googlesheets methods - https://www.python-engineer.com/posts/google-sheets-api/ , https://www.geeksforgeeks.org/using-google-sheets-as-database-in-python/
- For an explanation of datetime and date countdown - https://www.dataquest.io/blog/python-datetime/, https://docs.python.org/3/library/datetime.html
- For help with date validation - https://stackoverflow.com/questions/64601493/time-cannot-be-set-in-the-past-condition-python
- For explanation on OS and clear screen () - https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python
- For explanation on converting decimal time to mm:ss for the race pace calculations functions - https://stackoverflow.com/questions/32087209/converting-decimal-time-hh-hhh-into-hhmmss-in-python
- For explanation on converting strings to datetime objects - https://www.datacamp.com/tutorial/converting-strings-datetime-objects
- For an explanation on how to import and use termcolor - https://pypi.org/project/termcolor/
- For an explanation on the time.sleep() function - https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
