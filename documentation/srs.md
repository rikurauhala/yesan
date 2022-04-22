# Software requirements specification

## Purpose

The application is called **Yesan**, (예산, Korean for *budget*). Its purpose is to help its users to keep track of their personal finances and see where their money is going. The user interface is only available in English. The programming language used is Python and user data is stored in an SQLite database.

"No more spreadsheets!"

## User interface

The application has a graphical user interface created with the Tkinter library.

## Functionality

[ X ] = ready  
[ / ] = working on it

### Basic

- [ / ] Main view
  - Relevant information about user's personal finances
    - Monthly income
    - Monthly expenses
    - Net worth
  - [ X ] Contains buttons for adding new accounts and transactions
- [ / ] Account view
  - [ X ] Contains a list of accounts and their balance
  - [ X ] Displays net worth
  - [ X ] Adding new accounts
  - [ / ] Importing data from a csv file
  - [ X ] Exporting data into a csv file
- [ / ] Transaction view
  - [ X ] Lists recent transactions
  - [ X ] Adding transactions
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
