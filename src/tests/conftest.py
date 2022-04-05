from database.database_operations import initialize_database


def pytest_configure():
    initialize_database()
