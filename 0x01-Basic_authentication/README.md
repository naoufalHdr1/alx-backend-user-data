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
Run the app:
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```
Test with:
```bash
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```
Expect:
```json
{"error": "Unauthorized"}
```
