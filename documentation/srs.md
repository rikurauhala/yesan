# Software requirements specification

## Purpose

The application is called **Yesan**, (예산, Korean for *budget*). Its purpose is to help its users to keep track of their personal finances and see where their money is going. The application offers an alternative to the tedious task of managing personal finance data with software such as Microsoft Excel or LibreOffice Calc.

» "No more spreadsheets!"

## User interface

The application has a graphical user interface created with the `Tkinter` library. The user interface is only available in English.

## Functionality

 The programming language used is Python and user data is stored in an SQLite database via the `sqlite3` module. The application contains the following functionality. *Basic* functionality forms the core of the application and *secondary* features are ideas for further development.

[ X ] = ready  
[ / ] = working on it

### Basic

- [ / ] Main view
  - Relevant information about user's personal finances
    - Monthly income
    - Monthly expenses
    - Net worth
  - [ X ] Contains a button for showing the account view
  - [ X ] Contains a button for showing the transaction view
  - [ X ] Contains a button for exiting the application
- [ / ] Account view
  - [ X ] Contains a list of accounts and their balance
  - [ X ] Displays net worth
  - [ X ] Contains a button for adding new accounts
  - [ / ] Importing data from a csv file
  - [ X ] Exporting data into a csv file
- [ / ] Transaction view
  - [ X ] Contains a list of recent transactions
  - [ X ] Contains a button for adding new transactions
  - [ / ] Importing data from a csv file
  - [ X ] Exporting data into a csv file

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
