# Software requirements specification

## Purpose

The application is called *Yesan*, (예산, Korean for *budget*). Yesan is an application to help its users to track their personal finances and see where their money is going. The user interface is only available in English. The programming language used is Python and user data will be stored in an SQLite database.

No more spreadsheets!

## User interface

The application has a graphical user interface created with the Tkinter library.

## Functionality

### Basic

- Main view
  - Relevant information about user's personal finances
    - Monthly income
    - Monthly expenses
    - Net worth
- Transaction view
  - Adding transactions
  - Deleting/editing transactions
- Account view
  - Creating/deleting/editing accounts
  - An "account" (for lack of a better term) can be anything from a checking account to a wallet to cryptocurrency or other assets

### Secondary

- Login view
  - Password protection
  - Protecting sensitive personal data
    - Encrypting/decrypting the database (?)
- Budgeting
  - Creating a budget and comparing monthly expenses
- Reports
  - Generating monthly/yearly reports in txt/html/pdf etc. form
