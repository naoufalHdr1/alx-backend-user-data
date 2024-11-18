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

### Task 1:

Complete the `DB` class by implementing the `add_user` method. This method:

- Accepts `email` and `hashed_password` as string arguments.
- Creates and saves a `User` object to the database.
- Returns the created `User` object.

Running the script should display the IDs of the newly added users.
