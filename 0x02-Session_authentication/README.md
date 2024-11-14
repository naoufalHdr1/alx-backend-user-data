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
