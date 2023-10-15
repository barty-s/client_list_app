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

<img src='/docs/workflow.png' >

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

- I would like to allow for clients with no previous running experience, i.e. no PB, to be able to be added to the client list and to then develop the automated calculations to accomodate this feature.
- I would to create input and automated calculations options for other sports such as cycling, swimming, weight-lifting etc depending on the trainer's area of expertise and their clients' needs. This would involve optimizing the code into class objects for the new client and the specific sport or sports that they practice.
- I would like to improve the pb and goal time inputs to include "ss" to make their pace times more accurate.

- During testing it became apparent that if the race date falls into the past naturally, and then the user selects to view the client, the countdown will be a positive integer. To resolve this issue I would like to add new fuctions to deal with this scenario and I would also remove the Days Til Race column in the Googlesheet so that if the user is viewing that, they will not see the countdown, as it may not be accurate.

## Technologies

### Languages

- Python was solely used to create this app

### Programs

- Git - version control
- VSCode - as the program editor
- Black - Python auto formatter installed in VSCode
- PyLint - Code analyzer installed in VSCode to follow PEP 8 style guide
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
- time - To use the sleep() function to improve UX and slow down the speed of the messages being displayed.

## Testing

### Code Validation

- PyLint - this is a static code analyzer which I installed in VSCode. It highlights problems in the code and gives suggestions on how best to style the code so as to follow the PEP 8 recommended style.
- CI Python Linter https://pep8ci.herokuapp.com/

### Test Cases

#### Main Menu

1. The app opens with a welcome message and asks the user to choose an action from the list of options - Add a client, view a client, edit a client, delete a client and finally exit the app.

<img src='/docs/menu/main-menu.png' >

2. If the user types a number outside the range 1 - 5, they will be informed that their choice was invalid and then they will be prompted to choose again from the range of 1 - 5.

<img src='/docs/menu/main-menu-error.png' >

3. The user can choose to type a number or type out their choice e.g. "1" or "Add a client". It is not case sensitive, so the user can type in all lower case, or in capitals, or in a mix of the two, with no errors arising.

#### Action 1 - Add a client

##### Name

1. On selecting option one, the screen will be cleared and the user is prompted to type their client's First and Last names. The user must type two words only to match the specified pattern of "first + last" name.

<img src='/docs/action1/name.png' >

2. If the user types only one name, they will see a warning saying their input does not match the specified pattern.

<img src='/docs/action1/name1.png' >

3. If the user types three names, they will be similarly warned and prompted.

<img src='/docs/action1/name2.png' >

4. The user can type a mix of upper and lower cases and the output will be converted to a "First Last" pattern when all the client's information is displayed at the end.

<img src='/docs/action1/name3.png' > <img src='/docs/action1/name4.png' >

##### Email

5. The user is next asked to input the client's email address.

<img src='/docs/action1/email.png' >

The user must include a "@" symbol and a "." for the address to be valid, otherwise they will be warned and prompted to input a valid email address.

<img src='/docs/action1/email1.png' >

6. If the user inputs an email that already exists in the client list database (googlesheets), they will be warned and then the Main Menu will be displayed again.

<img src='/docs/action1/email2.png' >

##### Age

7. On entering a valid, unique email, the user will then prompted to input their client's age.
8. The user cannot input any letters, only whole numbers are accepted.

<img src='/docs/action1/age1.png' >

The user cannot input a number below 18 or above 100. They will be warned about their error and then prompted to input a valid, whole number age.

<img src='/docs/action1/age2.png' >

##### Distance

9. When the user has input a valid age, they are next prompted to choose their client's goal distance that they are training for from the list of race distance options. The user can choose between 5km, 10km, Half-Marathon, Marathon.

<img src='/docs/action1/distance.png' >

10. If the user inputs a value outside the range 1-4, they will be warned that their input is invalid and then prompted to input a valid number.

<img src='/docs/action1/distance1.png' >

11. The user can input a number or type out their choice in any combination of lower/uppercase text, and this will be accepted by the program.

<img src='/docs/action1/distance2.png' >

##### PB Time

12. On selecting their client's race distance, the user is then prompted to input their client's personal best time (PB) for the distance they have just input.
13. The user is shown a warning of the maximum time for the selected race distance. For example, a 5km race distance is limited to a 00:59 minute PB, as this is the typical cut off time for a 5km race.

<img src='/docs/action1/pb.png' >

14. If the user inputs an integer above 0 for the "hh" input, they will be warned that their input must be 0 at a maximum, so as not to exceed the 00:59 limit. The user can input 0 or 00 and both will be accepted. And for number below 10, it is not necessary to prefix with "0" e.g "7" is valid as is "07".

<img src='/docs/action1/pb1.png' >

15. If the user inputs an integer below 12 for the "mm" input, they will be warned that their input must be 12 at a minimum as there is a minimum limit of 00:12 mins for a 5km race, which is the current world record.

<img src='/docs/action1/pb2.png' >

16. If the user selected 10km as the race distance, there will be a minimum limit of 00:26 minutes, the current world record time, and a maximum limit of 00:59, the standard limit for a 10km race.
17. If the user selected Half-Marathon as the race distance, there will be a minimum limit of 00:57 minutes, the current world record time, and a maximum limit of 02:59, the standard limit for a half-marathon race.
18. If the user selected Marathon as the race distance, there will be a minimum limit of 02:00 hours, the current world record time, and a maximum limit of 06:59, the standard limit for a marathon race.
19. If the user inputs values outside the above-stated limits, they will be warned of either the maximum or minimum limit, and then prompted to input a valid value - as demonstrated with the 5km example images.

##### Goal Time

20. Once the user has input a valid PB time for the race distance, they will be prompted to input a goal time, that is the time their client hopes to complete the race in.

<img src='/docs/action1/gt.png' >

21. The exact same minimum and maximum limits, and invalid input warnings, are put on the goal time as on the PB time, as outlined above.

<img src='/docs/action1/gt1.png' >

##### Date of next race

22. The user is finally asked to input the date of their client's next race. The user must follow the format mm/dd/yyyy for the date to be accepted as valid.

<img src='/docs/action1/date.png' >

23. If the user inputs an invalid value for "mm", ie outside the range of 1-12, or for "dd", outside 1-31, they will be warned and prompted to input a valid date.

<img src='/docs/action1/date1.png' >

24. If the date is in the past or beyond the limit of 12/31/2030, the user will be warned and prompted to input a valid date.

<img src='/docs/action1/date2.png' >

##### Client successfully added

25. Once the final input has been accepted the user will see a message that the client is being added to the database.

<img src='/docs/action1/add.png' >

26. As long as all the values are valid, the user will then see a message confirming the client has been added to the database.

<img src='/docs/action1/ad1.png' >

27. A summary of the client's data will then be shown to the user. It will include all the input values, as well as the countdown of the number of days left until the client's race, their current running pace in minutes/km and their goal time race pace in minutes/km, which are calculated automatically by the program.

<img src='/docs/action1/client.png' >

28. The googlesheets client_list will be updated with this new client's data and the calculated countdown and race paces.

<img src='/docs/action1/db_new_client.png' >

29. The user will be shown the Main Menu again to choose to either continue with the program or to exit.

#### Action 2 - View a client

1. On selecting action 2, the screen will be cleared and the user will be prompted to input their client's email address.

<img src='/docs/action2/search.png' >

2. If the user inputs an invalid email, for example, missing the @ or ".", they will be warned of the error and prompted to input a valid email.

<img src='/docs/action2/search1.png' >

3. If the user inputs a email that doesn't exist in the database, they will be warned and then the main menu will be displayed.

<img src='/docs/action2/search2.png' >

4. When the user inputs a valid email that exists in the database, the "days until the next race" figure will be updated from today. The client's information will be displayed and the Main Menu will also be displayed.

<img src='/docs/action2/search3.png' >

#### Action 3 - Edit a client

1. On selecting action 3, the user will be prompted to input the client's email.
2. On inputting a valid email that exists in the database, the screen will be cleared and the searched client's data will be displayed, with the "Days until next race" having been updated from the present day. Below the client's data, the user will see a menu of elements to be edited, which are all of the inputs outlined in the "Add a Client" section of this README. The user also has a option to return to the Main Menu if they do not wish to edit anything.

<img src='/docs/action3/edit_menu.png' >

##### Edit Name

1. If the user selects to edit their client's name, they will be prompted to update the client's name. The same validation requirements are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_name.png' >

2. On inputting a valid First + Last name combination, the database will be updated and the client's updated data will be displayed along with the Main Menu.

<img src='/docs/action3/edit_name2.png' >
<img src='/docs/action3/edit_name1.png' >

##### Edit Email

3. If the user selects to edit their client's email address, they will be prompted to update the client's email address. The same validation requirements are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_email.png' >

4. On inputting a valid email address, the database will be updated and the client's updated data will be displayed along with the Main Menu.

<img src='/docs/action3/edit_email2.png' >
<img src='/docs/action3/edit_email1.png' >

##### Edit Age

5. If the user selects to edit their client's age, they will be prompted to update the client's age. The same validation requirements and minimum/maximum limits are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_age.png' >

6. On inputting a valid age, the database will be updated and the client's updated data will be displayed along with the Main Menu.

<img src='/docs/action3/edit_age2.png' >
<img src='/docs/action3/edit_age1.png' >

##### Edit Goal Distance

7. If the user selects to edit their client's goal distance, they will be warned that they will also need to edit their client's PB and Goal Time to correspond to the new goal distance. They will then be shown the race distance options list.

<img src='/docs/action3/edit_distance.png' >

8. On selecting a valid option from the list, the user will then be prompted to update their client's PB and Goal time for that distance. The same validation requirements and time limits are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_distance2.png' >

9. On entering valid time data, the database will be updated for distance, PB and goal time. The current race pace and goal race pace will also be updated in the database. The client's updated data will be displayed along with the Main Menu.

<img src='/docs/action3/edit_distance4.png' >
<img src='/docs/action3/edit_distance3.png' >

##### Edit Current PB

10. If the user selects to edit their client's current PB, they will be prompted to enter the new PB time. The same validation requirements and time limits are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_pb.png' >

11. On entering valid time data, the database will be updated with the new current PB. The current race pace will also be updated in the database. The client's updated data will then be displayed along with the Main Menu.

<img src='/docs/action3/edit_pb2.png' >
<img src='/docs/action3/edit_pb1.png' >

##### Edit Goal Time

12. If the user selects to edit their client's current goal time, they will be prompted to enter the new goal time. The same validation requirements and time limits are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_gt.png' >

13. On entering valid time data, the database will be updated with the new goal time. The goal race pace will also be updated in the database. The client's updated data will then be displayed along with the Main Menu.

<img src='/docs/action3/edit_gt2.png' >
<img src='/docs/action3/edit_gt1.png' >

##### Edit Next Race Date

14. If the user selects to edit their client's next race date, they will be prompted to enter the new race date. The same validation requirements and date limits are applied as outlined in the Add a Client section.

<img src='/docs/action3/edit_date.png' >

13. On entering a valid new date, the database will be updated with the new race date. The days until race countdown will also be updated in the database. The client's updated data will then be displayed along with the Main Menu.

<img src='/docs/action3/edit_date2.png' >
<img src='/docs/action3/edit_date1.png' >

#### Action 4 - Delete a client

1. On selecting action 4, the user will be prompted to input the client's email.
2. On inputting a valid email, the client's data will be displayed and the user will be asked if they are sure they want to delete the client.

<img src='/docs/action4/delete.png' >

3. The user can type 'n', 'no', 'y', 'yes' in any combination of upper/lower case letters and all answers will be accepted. If the user types anything else they will be warned and then prompted to type 'y/n'.

<img src='/docs/action4/delete1.png' >

4. If the user chooses not to delete a client, they will be shown a message stating the client has not been deleted and the main menu will be displayed. The database will not be affected.

<img src='/docs/action4/delete2.png' >
<img src='/docs/action4/delete3.png' >

5. If the user type "y" or any of the affirmative possibilities, they will be a shown a message confirming the client's data has been removed from the database and the Main Menu will be displayed. The database will be updated.

<img src='/docs/action4/delete4.png' >
<img src='/docs/action4/delete5.png' >

#### Action 5 - Exit

1. On selecting action 5, the user will be shown a signing-off message and the app will stop running.

<img src='/docs/action5/exit.png' >

### Bugs

#### Fixed

- Next Race Date validation - Originally, an if/else statement was included in the but that only checked once if the user had input a correct date, that is the user could first input an invalid date, be prompted to input a correct date, then input an invalid date again, and that would be accepted. So it was changed for a while loop to keep asking the user to input a date until it fits within the limits.
- Edit Race Date - to ensure the countdown days until the next race was also updated, a new function was needed to separate the update countdown and the append functions. This was useful as the update countdown function was then used in the display client option - the countdown days will be accurate to the day it is viewed.
- Enforce a minimum on the PB and Goal times - The user was able to input 00:01 for 5km/10km which doesn't make sense and produces strange race paces. Therefore, a minimum/maximum limit for each race was set. The minimum time is the current world record for each race distance and the maximum time is the standard limit participants have to complete the race in. Normally, in organised races, there is a bus that follows the race pack and if there are people who are running too slowly, they are picked up by the bus so that the streets aren't blocked to other users for too long.

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

## Acknowledgements

- mentor
- CI tutor Sarah
