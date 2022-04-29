CREATE TABLE accounts (
    id TEXT PRIMARY KEY,
    name TEXT,
    type TEXT
);

CREATE TABLE transactions (
    id TEXT PRIMARY KEY,
    date INTEGER,
    amount INTEGER,
    category TEXT,
    description TEXT,
    account_id TEXT REFERENCES accounts,
    party TEXT
);
