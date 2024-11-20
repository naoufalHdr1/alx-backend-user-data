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


### Task 8: Credentials validation

Develop the `valid_login` method in the `Auth` class to:

- Accept `email` and `password` as arguments.
- Locate the user by their email.
    - If the user exists, validate the password using `bcrypt.checkpw`.
    - Return `True` if the password matches, otherwise return `False`.
- If the user does not exist, return `False`.

Output:
- Matching credentials: `True`.
- Incorrect credentials or unknown email: `False`.

### Task 9: Generate UUIDs

Create the `_generate_uuid` method in the `auth` module that:

- Generates a new `UUID` using the `uuid` module.
- Returns the string representation of the new UUID.

Output:
- The method should return a valid UUID string when called.

### Task 10: Get Session ID

Create the `create_session` method in the `Auth` class that:

- Takes an `email` string as an argument.
- Finds the user corresponding to the given email.
- Generates a new UUID using the `_generate_uuid` method.
- Stores the new UUID as the `session_id` for the user in the database using a public method from `self._db`.
- Returns the session ID as a string.
- If the user does not exist, the method should return `None`.

Output:
- If the user is found and a session is created, return the new session ID (a string).
- If the user is not found, return `None`.

### Task 11: Log in

Implement a `login` function for the `POST /sessions` route:
- It should validate the email and password, create a session if valid, and return a success message with the session ID in a cookie.
- If credentials are incorrect, return a 401 Unauthorized status.

### Task 12: Find user by session ID

Implement the `get_user_from_session_id` method in the `Auth` class:
- It should take a `session_id` string, check for the corresponding user in the database, and return the user object.
- If the session ID is `None` or no user is found, return `None`. Only use public methods of `self._db`.

### Task 13: Destroy session

Implement the `destroy_session` method in the `Auth` class:
- It should take a `user_id` integer, find the corresponding `user`, and set the session ID to `None`.
- Ensure only public methods of `self._db` are used.

### Task 14: Log out

Implement a logout function in the Flask app to handle the `DELETE /sessions` route:
- The request will contain the session ID in the cookie.
- If a valid user is found with the session ID, destroy the session and redirect to the home page (`GET /`).
- If the session ID is invalid or no user is found, return a 403 HTTP status.

### Task 15: User Profile

Create the profile function to handle the `GET /profile` route:
- The function should expect the session ID in the request's cookies.
- If the session ID is valid and corresponds to an existing user, return a JSON response with the user's email and a 200 HTTP status.
- If the session ID is invalid or the user does not exist, return a 403 HTTP status.

Output:
- The script should return the user's email when the session ID is valid and respond with a 403 status if the session ID is invalid or not found.

### Task 16: Generate reset password token

Create the `get_reset_password_token` method in the `Auth` class to:
- Accept an email string as an argument.
- Find the user corresponding to the email.
- If the user does not exist, raise a `ValueError` exception.
- If the user exists, generate a new UUID, update the user's `reset_token` field in the database, and return the token.

Output:
The script should return a UUID as the reset token for the user, and raise a `ValueError` if the user does not exist.

### Task 17: Get reset password token

Create the `get_reset_password_token` function to:
- Respond to the `POST /reset_password` route.
- Expect form data with an "email" field.
- If the email is not registered, respond with a 403 status code.
- If the email is registered, generate a reset token, update the user's `reset_token` field, and respond with a 200 HTTP status along with the following JSON payload:
```json
{"email": "<user email>", "reset_token": "<reset token>"}
```

Output:
- The script should return a 200 status with a reset token if the email is valid, or a 403 status if the email is not found.

### Task 18: Update password

Create the `update_password` method in the `Auth` class to:

- Accept a `reset_token` string and a `password` string as arguments.
- Use the `reset_token` to find the corresponding user.
- If the user does not exist or the token is invalid, raise a `ValueError` exception.
- If the user is found, hash the new password and update the user's `hashed_password` field with the new hash.
- Set the `reset_token` field to `None` to indicate the password has been reset.

Output:
- The method should update the user's password and reset the token. If no user is found with the provided `reset_token`, raise a `ValueError`.

### Task 19: Update password end-point

Create the `update_password` function in the `app` module to:
- Handle the `PUT /reset_password` route.
- The request should contain form data with fields: `"email"`, `"reset_token"`, and `"new_password"`.
- Use the `reset_token` to find the corresponding user.
- If the token is invalid (no user found or token mismatch), catch the exception and respond with a 403 HTTP status code.
- If the token is valid, update the user's password and return a 200 HTTP status code with the following JSON payload:
```json
{"email": "<user email>", "message": "Password updated"}
```

Output:
- The function should properly handle both valid and invalid tokens, ensuring the password is updated or the appropriate error is returned.

### Task 20: End-to-end integration test `#Advanced`

Create a `main.py` module to test your Flask app's endpoints using the `requests` library. Each function will make HTTP requests to corresponding endpoints and validate responses with assertions.

Functions to Implement:
1. `register_user(email, password)`: Tests user registration (`/register`).
2. `log_in_wrong_password(email, password)`: Tests login with incorrect credentials (`/sessions`).
3. `log_in(email, password)`: Tests login with correct credentials and returns session ID.
4. `profile_unlogged()`: Tests access to `/profile` without a session (should fail).
5. `profile_logged(session_id)`: Tests access to `/profile` with a valid session.
6. `log_out(session_id)`: Tests logging out (`/sessions`).
7. `reset_password_token(email)`: Gets a reset token (`/reset_password`).
8. `update_password(email, reset_token, new_password)`: Updates the user's password.

Outcome:
- Running `python main.py` tests all endpoints.
- No output means all tests passed; failures raise an `AssertionError`.
