# Software requirements specification

## Purpose

The application is called **Yesan** (예산, Korean for *budget*). Its purpose is to help its users to keep track of their personal finances and see where their money is going. The application offers an alternative to the tedious task of managing personal finance data with software such as Microsoft Excel or LibreOffice Calc.

» "No more spreadsheets!"

## User interface

The application has a graphical user interface created with the `tkinter` library. The user interface is only available in English. The only supported currency is the euro (€).

## Functionality

The programming language used is Python and user data is stored in an SQLite database via the `sqlite3` module. Data may also be imported and exported in the csv file format. The application contains the following functionality. *Basic* functionality forms the core of the application and *secondary* features are ideas for further development.

[ X ] = ready  
[ / ] = working on it

### Basic

- [ X ] Main view
  - [ X ] Contains "Accounts" button for showing the account view
    - [ X ] Account view
      - [ X ] Contains a list of accounts and their balance
      - [ X ] Displays net worth
      - [ X ] Contains button "Back" for going back to main view
      - [ X ] Contains button "New account" for showing the new account view
          - [ X ] New account view
            - [ X ] Contains fields for account details
            - [ X ] Contains button "Back" for going back to the account view
            - [ X ] Contains button "Submit" for adding a new account 
      - [ X ] Contains button "Import" for importing account data from a csv file
      - [ X ] Contains button "Export" for exporting account data into a csv file
  - [ X ] Contains button "Transactions" for showing the transaction view
    - [ X ] Transaction view
      - [ X ] Contains a list of recent transactions
      - [ X ] Contains button "New transaction" for adding new transactions
          - [ X ] New transaction view
                - [ X ] Contains fields for transaction details
                - [ X ] Contains button "Back" for going back to the transaction view
                - [ X ] Contains button "Submit" for adding a new transaction 
      - [ X ] Contains button "Import" for importing transaction data from a csv file
      - [ X ] Contains button "Export" for exporting transaction data into a csv file
  - [ X ] Contains button "Quit" for exiting the application

### Secondary

- Login view
  - Password protection
  - Protecting sensitive personal data
    - Encrypting/decrypting the database (?)
- Budgeting
  - Creating a budget and comparing monthly expenses
- Reports
  - Generating monthly/yearly reports in txt/html/pdf etc. form
- Support for other languages and currencies
