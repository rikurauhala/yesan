CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    timestamp INTEGER,
    amount INTEGER,
    category TEXT,
    description TEXT,
    account_id INTEGER REFERENCES accounts,
    party TEXT
);
