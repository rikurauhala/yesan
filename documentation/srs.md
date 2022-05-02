# Software requirements specification

## Purpose

The application is called **Yesan** (예산, Korean for *budget*). Its purpose is to help its users to keep track of their personal finances and see where their money is going. The application offers an alternative to the tedious task of managing personal finance data with software such as Microsoft Excel or LibreOffice Calc.

» "No more spreadsheets!"

## User interface

The application has a graphical user interface created with the `tkinter` library. The user interface is only available in English. The only supported currency is the euro (€).

## Functionality

The programming language used is Python and user data is stored in an SQLite database via the `sqlite3` module. Data may also be imported and exported in the csv file format. The application contains the following functionality. *Primary* functionality forms the core of the application and *secondary* features are ideas for further development.

### Primary

All of the following functionality has been implemented. This list represents the current state of the application.

- Main view
  - Contains "Accounts" button for showing the account view
    - Account view
      - Contains a list of accounts and their balance
      - Displays net worth
      - Contains button "Back" for going back to main view
      - Contains button "New account" for showing the new account view
          - New account view
            - Contains fields for account details
            - Contains button "Back" for going back to the account view
            - Contains button "Submit" for adding a new account 
      - Contains button "Import" for importing account data from a csv file
      - Contains button "Export" for exporting account data into a csv file
  - Contains button "Transactions" for showing the transaction view
    - Transaction view
      - Contains a list of recent transactions
      - Contains button "New transaction" for adding new transactions
          - New transaction view
            - Contains fields for transaction details
            - Contains button "Back" for going back to the transaction view
            - Contains button "Submit" for adding a new transaction 
      - Contains button "Import" for importing transaction data from a csv file
      - Contains button "Export" for exporting transaction data into a csv file
  - Contains button "Quit" for exiting the application

### Secondary

This list contains ideas for functionality to be implemented at a later date.

- Login view
  - Password protection
  - Protecting sensitive personal data
    - Encrypting/decrypting the database (?)
- Individual account view
  - View transaction history and other statistics of each individual account
- Budgeting
  - Creating a budget and comparing monthly expenses
- Reports
  - Generating monthly/yearly reports in txt/html/pdf etc. form
- Support for other languages and currencies
