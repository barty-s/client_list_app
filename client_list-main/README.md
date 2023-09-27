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

The purpose of this app is to allow a trainer to access their list of clients for running training. The user i.e. the trainer, can add new clients, view clients, edit a client's information and delete a client, as needed. There are also automated calculations done on the inputted data to determine the running training needs of the client which will assist the trainer in making a training plan for their client.

## Credits

- CI run-through project - Code to access APIs and Google Sheets
