# 0x01. Basic Authentication

This project demonstrates the basics of implementing authentication on a simple API in Python. It covers fundamental concepts of Basic Authentication, HTTP headers, and security checks using Flask, with a particular focus on managing and securing API endpoints.

# Project Overview

This project introduces Basic Authentication by building an authentication layer on a sample API. In a real-world context, Basic Authentication would typically be managed using external libraries like `Flask-HTTPAuth` for security and efficiency. However, for educational purposes, this project builds the authentication system from the ground up.

# Background Context

The project focuses on:

- Understanding the authentication process and its importance.
- Creating custom error handlers for HTTP status codes.
- Implementing Basic Authentication manually, including encoding, decoding, and handling requests.

# Learning Objectives

By the end of this project, you should be able to:

- Explain the concept and purpose of authentication.
- Understand and utilize Base64 encoding.
- Define Basic Authentication and understand how it works in HTTP headers.
- Configure HTTP headers, particularly the Authorization header.

# Tasks

## Task 0: Simple-basic-API

1. **Download:** Extract [archive.zip](https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA) with a simple API and User model.
2. **Install:** Run `pip3 install -r requirements.txt`.
3. **Start Server:** Set `API_HOST=0.0.0.0` and `API_PORT=5000`, then run `python3 -m api.v1.app`.
4. **Test:** Use `curl http://0.0.0.0:5000/api/v1/status` to check for `{"status":"OK"}`.

## Task: 401 Unauthorized Error Handler

1. Update `api/v1/app.py`:
    - Add an error handler for 401 status code, returning: `{"error": "Unauthorized"}` using Flask's `jsonify`.

2. Create Endpoint:
    - In `api/v1/views/index.py`, add a `GET /api/v1/unauthorized` route that triggers a 401 error with `abort(401)`.

3. Test:
- Run the app:
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```
- Test with:
```bash
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```
- Expect:
```json
{"error": "Unauthorized"}
```

## Task 2: Error handler: Forbidden

1. Update `api/v1/app.py`:
    - Add an error handler for the 403 status code, returning: `{"error": "Forbidden"}` using Flask's `jsonify`.

2. Create Endpoint:
    - In `api/v1/views/index.py`, add a `GET /api/v1/forbidden` route that triggers a 403 error with `abort(403)`.

3. Test:
- Run the app:
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```
- Test with:
```bash
curl "http://0.0.0.0:5000/api/v1/forbidden"
```
- Expect:
```json
{"error": "Forbidden"}
```

## Task 3: Auth class

1. Folder and File Creation:
- Create a folder `api/v1/auth`.
- Inside it, create an empty file `api/v1/auth/__init__.py`.

2. Class Definition:
- In `api/v1/auth/auth.py`, define a class `Auth` with the following methods:
    - `require_auth(self, path: str, excluded_paths: List[str]) -> bool`:
    Returns `False` (`path` and `excluded_paths` are placeholders for future implementation).
    - `authorization_header(self, request=None) -> str`:
    Returns `None` (request is the Flask request object).
    - `current_user(self, request=None) -> TypeVar('User')`:
    Returns `None` (request is the Flask request object).

3. Testing:

- Run a `main_0.py` file from `mains/`:
- Expected output:
```bash
False
None
None
```

## Task 4:  Define which routes don't need authentication

1. Method Update:
Update the `require_auth(self, path: str, excluded_paths: List[str]) -> bool` method in the `Auth` class with the following logic:
- Return `True` if `path` is `None`.
- Return `True` if `excluded_paths` is `None` or empty.
- Return `False` if `path` is in `excluded_paths`.
- Ensure the method is slash tolerant:
    - If `path = /api/v1/status` and `excluded_paths` contains `/api/v1/status/`, it should return `False` because the path `/api/v1/status` and `/api/v1/status/` are considered equivalent.

2. Test Script:
- Run `main_1.py` file in `/mains`:
- Expected Output:
```bash
True
True
True
False
False
True
True
```

## Task 5: Request validation!

1. Update `authorization_header`:
- Return `None` if `request` is `None` or missing `Authorization` header; otherwise, return the header’s value.

2. Configure `auth` in `api/v1/app.py`:
- Set `auth` based on `AUTH_TYPE` environment variable (initialize `Auth` if needed).

3. Filter Requests with `before_request`:
- Skip filtering if `auth` is `None` or `request.path` is allowed (`/api/v1/status/`, `/api/v1/unauthorized/`, `/api/v1/forbidden/`).
- Check if path requires auth using `auth.require_auth`.
- If `auth.authorization_header(request)` is `None`, abort with `401`.
- If `auth.current_user(request)` is `None`, abort with `403`.

4. Testing:
- Start server with `AUTH_TYPE=auth`, then test:
`/api/v1/status`: Returns `{"status": "OK"}`.
`/api/v1/users` without Authorization: `{"error": "Unauthorized"}`.
`/api/v1/users` with Authorization: `{"error": "Forbidden"}`.

## Task 6: Basic auth

1. Create BasicAuth Class:
- Add a new class `BasicAuth` inheriting from `Auth` in `api/v1/auth/basic_auth.py`. For now, this class remains empty.

2. Update `api/v1/app.py` to Use BasicAuth:
- Import `BasicAuth` if `AUTH_TYPE` is set to `"basic_auth"`.
- Initialize auth as an instance of `BasicAuth` if `AUTH_TYPE` is `"basic_auth"`; otherwise, continue using `Auth`.

## Task 7: Basic - Base64 part

Create the `extract_base64_authorization_header` method within the `BasicAuth` class to parse and return the Base64-encoded part of the Authorization header for Basic Authentication:
- Return `None` if the header is `None`, not a string, or doesn’t start with `"Basic "`.
- Otherwise, return the part of the header after `"Basic "`.

## Task 8: Basic - Base64 decode

Add a method `decode_base64_authorization_header` in the `BasicAuth` class to decode a Base64 string:
- Return `None` if `base64_authorization_header` is `None`, not a string, or not valid Base64 (use `try/except` for validation).
- Otherwise, return the decoded string in UTF-8 format `(decode('utf-8'))`.

This prepares the BasicAuth class for handling Base64-encoded credentials in Basic Authentication headers.

## Task 9: Basic - User credentials

Add the `extract_user_credentials` method in the `BasicAuth` class to retrieve the user email and password from a decoded Base64 string:
- Return `(None, None)` if `decoded_base64_authorization_header` is `None`, not a string, or doesn't contain a colon (`:`).
- Otherwise, split the string at the colon and return the email and password as a tuple.

This prepares the BasicAuth class to handle and parse credentials from Basic Authentication headers.

## Task 10: Basic - User object

Add the `user_object_from_credentials` method in the BasicAuth class to retrieve a `User` instance based on the provided email and password:
- Return `None` if the `user_email` or `user_pwd` is `None` or not a string.
- Return `None` if the user with the given email doesn't exist in the database (using `User.search` method).
- Return `None` if the password doesn't match the user's stored password (using the `is_valid_password method`).
- Otherwise, return the `User` instance found in the database.

This method helps validate the credentials and fetch the corresponding user object.

## Task 11: Basic - Overload `current_user` - and BOOM!

Add the `current_user` method to the `BasicAuth` class to overload the `Auth` class and retrieve the current `User` instance for a request:
1. Use the `authorization_header` from the request.
2. Use the `extract_base64_authorization_header` method to get the Base64-encoded part of the header.
3. Decode the Base64 string using `decode_base64_authorization_header`.
4. Extract the user credentials (email and password) from the decoded string using `extract_user_credentials`.
5. Retrieve the corresponding User object using `user_object_from_credentials`.

With this update, the API is fully protected by Basic Authentication. The `current_user` method allows the API to identify and authenticate users based on the provided credentials.

## Task 12: Basic - Allow password with ":" `#advanced`

Modify the `extract_user_credentials` method in the `BasicAuth` class to correctly parse passwords containing colons (`:`) from the Base64 decoded authorization header. The method should split the string at the first colon, allowing passwords with colons to be handled properly.
