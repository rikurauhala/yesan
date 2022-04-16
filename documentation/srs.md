# Software requirements specification

## Purpose

The application is called **Yesan**, (예산, Korean for *budget*). Its purpose is to help its users to keep track of their personal finances and see where their money is going. The user interface is only available in English. The programming language used is Python and user data is stored in an SQLite database.

"No more spreadsheets!"

## User interface

The application has a graphical user interface created with the Tkinter library.

## Functionality

[ ✔ ] = ready  
[ / ] = working on it

### Basic

- [ / ] Main view
  - Relevant information about user's personal finances
    - Monthly income
    - Monthly expenses
    - Net worth
  - [ ✔ ] Contains buttons for adding new accounts and transactions
- [ ✔ ] Account view
  - [ ✔ ] Contains a list of accounts and their balance
  - [ ✔ ] New account view
    - Used to add a new account to the database
  - An "account" (for lack of a better term) can be anything from a checking account to a wallet to cryptocurrency or other assets
- [ / ] Transaction view
  - [ ✔ ] Lists recent transactions
  - [ ✔ ] Adding transactions
  - Deleting/editing transactions

### Secondary

- Login view
  - Password protection
  - Protecting sensitive personal data
    - Encrypting/decrypting the database (?)
- Budgeting
  - Creating a budget and comparing monthly expenses
- Reports
  - Generating monthly/yearly reports in txt/html/pdf etc. form
