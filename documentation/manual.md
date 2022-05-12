# User manual

## Getting started

Before running the application for the first time, you need to run few commands to make sure everything works as expected. First, run `poetry install` to install dependencies. Then, run `poetru run invoke init` to initialize the database. You are now ready to start using the application. Run `poetry run invoke start` to enter the graphical user interface.

## User interface

This section contains screenshots of the application, captured on a machine running Cubbli Linux with the i3 window manager. Please note, that the application may look different depending on the operating system.

### Main view

![Screenshot of the main view](images/main_view.png)

The main view has four buttons. Clicking the `Accounts` button will take you to the Account view and clicking the `Transactions` button will take you to the Transaction view. The `Settings` button will display the Settings view that allows user to edit the configuration file of the application. Pressing the `Quit` button will ask for confirmation to terminate the program.

### Account view

![Screenshot of the account view](images/account_view.png)

When you first run the application, the account view should be empty. After adding accounts and transactions the view will start to make more sense. The account view offers a clear picture of your net worth and current status of all your accounts, assets, loans and so on. To add your first account, click the `+ New account` button.

### New account view

![Screenshot of the new account view](images/new_account_view.png)

To add a new account, fill in the fields for the name and the type of the account. Then click `Submit`. You may add more accounts or go back to the account view by pressing the `Back` button.

### Transaction view

![Screenshot of the transaction view](images/transaction_view.png)

The transaction view consists of more data than the account view. All your transactions will show up here. Latest transactions will always show up at the top. Red color indicates a negative transaction, as in money being sent away from you.

### New transaction view

![Screenshot of the new transaction view](images/new_transaction_view.png)

This view works just like the new account view, but more information is required. To add a new transaction, you first need to have at least one account added. If you try to add invalid data, the application should display a helpful message in red.

### Settings view

![Screenshot of the settings view](images/settings_view.png)

The settings view contains the contents of the .env file. You may edit the contents of the file either inside this view, or by opening the file itself with your favorite text editor. Pressing the `Save` button will write all changes to the .env file. Please do not edit the rows that start with the # symbol! Those are just helpful comments with no actual functionality! If you made a mistake, you can always hit the `Reset` button to start over with the default settings.
