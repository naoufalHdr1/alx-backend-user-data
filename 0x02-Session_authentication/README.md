# 0x02. Session Authentication
`#Back-end` `#Authentication`

This project demonstrates how to build a custom session authentication system using Python, without relying on external libraries or modules. The primary goal is to understand session authentication by implementing it from scratch in a backend environment.

## Project Overview

This project introduces session authentication in a REST API context, where each step of the process is built and explained. Session authentication is a common technique used to keep track of users across multiple requests by leveraging session cookies.

In a real-world application, it's best to use established libraries (e.g., Flask-HTTPAuth in Flask) to manage session authentication securely and efficiently. However, in this project, we manually create each component to gain a deeper understanding of session authentication mechanisms.

## Learning Objectives

By the end of this project, you should be able to:

- Define authentication and session authentication
- Understand what cookies are and how they work in session management
- Send cookies and parse cookies in a Flask application
- Describe the basic concepts behind session-based authentication

## Key Concepts

- **Session Authentication:** This authentication technique uses cookies to manage user sessions. When a user logs in, a session cookie is created and sent to the client, which includes it in subsequent requests to authenticate itself.

- **Cookies:** Cookies are small pieces of data stored by the client, often used in session management. They allow servers to track user state and maintain sessions across multiple requests.

- **Sending and Parsing Cookies:** This project covers both sending cookies from the server to the client and parsing cookies from client requests to manage authentication states.

## Tasks

### Task 0: Et moi et moi et moi!

Extend the Basic Authentication project by adding a `GET /users/me` endpoint to fetch the authenticated user as JSON.

Key Steps:

- **New Endpoint:** Implement `GET /users/me` to return the authenticated user.
- **Setup:** Copy previous project files and ensure all mandatory tasks are completed.
- **Modify** `request.current_user`: Update `@app.before_request` in `api/v1/app.py` to assign `auth.current_user(request)` to `request.current_user`.
- **Route Update:** Adjust `GET /api/v1/users/<user_id>`:
    - If `<user_id>` is `"me"` and `request.current_user` is `None`, return `404`.
    - If `"me"` and `request.current_user` is set, return the authenticated user.

### Task 1: Empty session

Create a new `SessionAuth` class for session-based authentication, inheriting from the `Auth` class. Configure the app to use `SessionAuth` if the `AUTH_TYPE` environment variable is set to `"session_auth"`.

Steps:

- **Create `SessionAuth` Class**: Define an empty `SessionAuth` class that inherits from `Auth` to set up session-based authentication.
- **Switch Authentication Types:** Update `api/v1/app.py` to check `AUTH_TYPE`:
    - Import and assign `SessionAuth` to `auth` if `AUTH_TYPE` is `"session_auth"`.
    - Otherwise, retain the previous authentication mechanism.
- **Test:** Validate the `SessionAuth` implementation by setting `AUTH_TYPE=session_auth` and confirming the expected responses for authorized and unauthorized requests.

### Task 2: Create a session

Enhance the `SessionAuth` class to manage user sessions using a dictionary for storing session data.

1. User-Session Mapping:
Add a class attribute `user_id_by_session_id`, initialized as an empty dictionary, to map Session IDs to user IDs.

2. Session Creation:
Implement `create_session(user_id: str)` to:
- Return `None` if `user_id` is invalid.
- Generate a unique Session ID using `uuid4()`.
- Map the Session ID to the `user_id` in the `user_id_by_session_id` dictionary.
- Allow multiple Session IDs per `user_id`.

This update enables in-memory session management and retrieval of `user_id` using Session IDs.


### Task 3: User ID for Session ID

Enhance the `SessionAuth` class with a method to retrieve the user ID linked to a session ID.

1. User ID Retrieval:
Add a method `user_id_for_session_id(self, session_id: str)` to:
- Return `None` if `session_id` is `None` or not a string.
- Use `.get()` to fetch the user ID associated with the given `session_id` from the `user_id_by_session_id` dictionary.

This addition complements the `create_session` method, allowing seamless storage and retrieval of user-session relationships.
