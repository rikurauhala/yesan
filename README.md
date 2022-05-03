## About

**Yesan** (예산, Korean for *budget*) is a personal finance application written in Python.

## Releases

- [Viikko 6](https://github.com/rikurauhala/yesan/releases/tag/viikko6) [latest]
- [Viikko 5](https://github.com/rikurauhala/yesan/releases/tag/viikko5)

## Documentation

- [Architecture](/documentation/architecture.md)
- [Changelog](/documentation/changelog.md)
- [Software requirements specification](documentation/srs.md)
- [User manual](documentation/manual.md)
- [Work hour tracking](documentation/tracking.md)

## Instructions

### Installing

```bash
# Get the source code
$ git clone git@github.com:rikurauhala/yesan.git

# Change directory
$ cd yesan

# Install dependencies
$ poetry install

# Initialize the database
$ poetry run invoke init
```

### Running
```bash
# Run the application
$ poetry run invoke start
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
