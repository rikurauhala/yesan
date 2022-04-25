# Architecture

## Functionality

### Creating a new account

The diagram below depicts a scenario in which a user creates a new account in the NewAccountView. First the user tries to create a new account, but hasn't specified its type. The user then sees an error message and enters the missing parameter. A new account is created by calling the create_account() function of the account service. The function passes its parameters to the class AccountRepository, which then creates a new account in the database and returns True. Finally, a message is displayed to the user indicating that a new account was succesfully created.

```mermaid
sequenceDiagram
    actor User
    participant NewAccountView
    participant AccountService
    participant AccountRepository
    User->>NewAccountView: click "Submit" button
    NewAccountView--XAccountService: create_account("Checking account")
    NewAccountView->>NewAccountView: display_message("error")
    NewAccountView->>AccountService: create_account("Checking account", "Bank account")
    AccountService->>AccountRepository: create("Checking account", "Bank account")
    AccountRepository-->>AccountService: True
    AccountService-->>NewAccountView: True
    NewAccountView->>NewAccountView: display_message("success")
```

## Entities

The application uses the following entities. An `account` can be anything from a bank account, to crypto currency or a loan. A `transaction` contains information about a single transaction where money is moved from one account to another, for example when receiving the monthly salary from the employer or making a purchase at the grocery store. Each account can be connected to multiple transactions and a single transaction can be only connected to one account.

```mermaid
classDiagram
    Transaction "*" --> "1" Account
    class Account {
        id
        name
        type
    }
    class Transaction {
        id
        timestamp
        amount
        category
        description
        account_id
        party
    }
```
