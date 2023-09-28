## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

# Client List App

The purpose of this app is to allow a trainer to access their list of clients for running training. The user i.e. the trainer, can add new clients, view clients, edit a client's information and delete a client, as needed. There are also automated calculations done on the inputted data to determine the training needs of the client which will assist the trainer in making a training plan for their client. It is assumed that a new client has previous running experience and is hiring this trainer to improve their running time, therefore all inputs must be completed.

## Future Features

- to allow for clients with no previous running experience
- to create options for other sports such as cycling, swimming, weight-lifting depending on the trainer's area of expertise

## Credits

- CI run-through project - Code to access APIs and Google Sheets
- https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response - for info on input validation
