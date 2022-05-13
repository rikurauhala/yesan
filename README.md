## About

**Yesan** (예산, Korean for *budget*) is a personal finance application written in Python. The application has a graphical user interface created with the `tkinter` library. User data is stored in an SQLite3 database.

## Releases

- [Loppupalautus](https://github.com/rikurauhala/yesan/releases/tag/loppupalautus) [latest]
- [Viikko 6](https://github.com/rikurauhala/yesan/releases/tag/viikko6)
- [Viikko 5](https://github.com/rikurauhala/yesan/releases/tag/viikko5)

## Documentation

- [Architecture](/documentation/architecture.md)
- [Changelog](/documentation/changelog.md)
- [Software requirements specification](documentation/srs.md)
- [Testing](documentation/testing.md)
- [User manual](documentation/manual.md)
- [Work hour tracking](documentation/hours.md)

## Instructions

See the [manual](documentation/manual.md) for more instructions.

### Installing

```bash
# Get the source code
$ git clone git@github.com:rikurauhala/yesan.git

# Change directory
$ cd yesan

# Install dependencies
$ poetry install

# Initialize the database
$ poetry run invoke build
```

### Running

```bash
# Run the application
$ poetry run invoke start

# There is also an option run a demonstration to see how the application works
# with some pre-filled data. Execute these commands to run the app in a demo mode.
# Then go to the account view and the transaction view and click "Import".

# Make the file executable
$ chmod +x demo.sh

# Run the application
$ ./demo.sh
```

### Testing

```bash
# Run tests
$ poetry run invoke test

# Create a test coverage report
$ poetry run invoke coverage-report

# Check quality of the code
$ poetry run invoke lint
```
