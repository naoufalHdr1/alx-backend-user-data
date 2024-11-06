# 0x00 Personal Data Project

## Project Overview

This project focuses on securely handling personal data and protecting Personally Identifiable Information (PII). You will learn to work with sensitive data, set up logging with obfuscation, handle authentication securely using environment variables, and connect to a database while following best practices.

## Learning Objectives

By the end of this project, you should understand:

1. What constitutes PII and examples of such information.
2. How to implement logging that obfuscates PII fields.
3. How to encrypt and verify passwords.
4. How to securely connect to a database using environment variables.

## Project Structure

- **filtered_logger.py:** Contains logging functionalities with data obfuscation, formatter setup, and logger configuration.
- **database connection:** Retrieves database credentials from environment variables to securely connect to a MySQL database.

## Tasks

### Task 0: `filter_datum` Function

Implements the `filter_datum` function, which:

- Takes a list of PII fields and replaces them in a log message with a placeholder string.
- Uses a regular expression to substitute sensitive fields.

### Task 1: `RedactingFormatter` Class

Creates a custom formatter that:

- Obfuscates specific fields in a log message.
- Uses the `filter_datum` function for filtering.
- Sets a logging format.

### Task 2: `get_logger` Function

Defines a logger configuration that:

- Logs up to `INFO` level.
- Has a `StreamHandler` with the `RedactingFormatter`.
- Does not propagate to other loggers.

### Task 3: `get_db` Function

Establishes a database connection:

- Uses `mysql-connector-python` to connect to a MySQL database.
- Retrieves credentials securely from environment variables:
    - `PERSONAL_DATA_DB_USERNAME`
    - `PERSONAL_DATA_DB_PASSWORD`
    - `PERSONAL_DATA_DB_HOST`
    - `PERSONAL_DATA_DB_NAME`

### Task 4: `main` Function

Implements a main function to:

- Connect to the database.
- Retrieve and log user data with PII fields obfuscated.

### Task 5: Encrypting Passwords

Implement a `hash_password` function that expects one string argument name password and returns a salted, hashed password, which is a byte string.

Implementation Notes:
- The `hash_password` function expects one string argument, `password`.
- It uses the `bcrypt.hashpw` method to hash the password with a generated salt, returning a byte string.

### Task 6: Check Valid Password

Implement an `is_valid` function that expects 2 arguments and returns a boolean.

Arguments:
- `hashed_password`: bytes type
- `password`: string type

Use bcrypt to validate that the provided password matches the hashed password.

## Usage

### Prerequisites

1. Install dependencies:
```bash
pip install mysql-connector-python
```

2. Set up environment variables for database authentication:
```bash
export PERSONAL_DATA_DB_USERNAME="your_username"
export PERSONAL_DATA_DB_PASSWORD="your_password"
export PERSONAL_DATA_DB_HOST="your_host"
export PERSONAL_DATA_DB_NAME="your_database"
```

### Running the Project

Execute Task Scripts:
```bash
./filtered_logger.py
```

## Resources

[What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/)\
[Python Logging Documentation](https://docs.python.org/3/library/logging.html)\
[bcrypt Python Package](https://github.com/pyca/bcrypt/)\
[Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo)
