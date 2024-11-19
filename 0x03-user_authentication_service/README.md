# 0x03. User Authentication Service

## Description

This project is a step-by-step implementation of a basic user authentication service using Python and Flask. It is intended for learning purposes to provide a clear understanding of how authentication mechanisms work by building one from scratch.

While in real-world applications it is recommended to use established modules or frameworks (e.g., Flask-User), this project offers a hands-on approach to fundamental authentication concepts.

## Learning Objectives

By completing this project, you will learn how to:

- Declare API routes in a Flask application.
- Get and set cookies in HTTP responses.
- Retrieve form data from requests.
- Return various HTTP status codes.
- Implement secure user authentication practices.

## Tasks

### Task 0: User model

Build a `User` model mapped to the `users` table with these attributes:

- `id`: Primary key, integer.
- `email` and `hashed_password`: Non-nullable strings.
- `session_id` and `reset_token`: Nullable strings.

The script should print the table name and column details.

### Task 1: Create user

Complete the `DB` class by implementing the `add_user` method. This method:

- Accepts `email` and `hashed_password` as string arguments.
- Creates and saves a `User` object to the database.
- Returns the created `User` object.

Running the script should display the IDs of the newly added users.

### Task 2: Find user

Develop the `find_user_by` method in the `DB` class to:

- Accept arbitrary keyword arguments for filtering rows in the `users` table.
- Return the first matching row or raise:
    - `NoResultFound` if no matching row is found.
    - `InvalidRequestError` for invalid query arguments.

The script should demonstrate successful user retrieval, handle cases where no user is found, and handle invalid query arguments gracefully.

### Task 3: Update user

Create the `update_user` method in the `DB` class to:

- Accept a `user_id` (integer) and arbitrary keyword arguments.
- Use `find_user_by` to locate the user and update their attributes.
- Commit the changes to the database.
- Raise a `ValueError` if an invalid attribute is passed.

The script should demonstrate successful user updates and raise an error for invalid attributes.

### Task 4: Hash password

Create a `_hash_password` method to:

- Accept a password string as input.
- Return a salted hash of the password as bytes, using `bcrypt.hashpw`.

The script should demonstrate the method returning a correctly hashed password in bytes.

### Task 5: Register user

Add a `register_user` method to the Auth class that:

- Accepts `email` and `password`.
- Raises `ValueError: User <email> already exists` if the email is already in use.
- Hashes the password with `_hash_password`, saves the user via `self._db`, and returns the `User` object if the email is new.

Output;
- Returns the `User` object if created.
- Raises `ValueError` if the email already exists.

### Task 6: Basic Flask app

Create a Flask app with:

- A single GET route ("/") that returns a JSON response: {"message": "Bienvenue"}
- Code to run the app on host="0.0.0.0" and port=5000.

Output:

- When accessing http://0.0.0.0:5000/, the response is: {"message": "Bienvenue"}

### Task 7: Register user

Create a `POST /users` route that:

- Expects form data fields: `"email"` and `"password"`.
- Uses the `Auth` class to register a new user.

Output:
- Successful registration:
```json
{"email": "bob@me.com", "message": "user created"}
```
- Duplicate registration:
```json
{"message": "email already registered"}
```
HTTP status: `400`
