# Expense Tracker API

## Overview

The **Expense Tracker API** is a simple and efficient system designed to help users manage and track their personal expenses. It provides functionality to categorize expenses, filter them based on time ranges, and maintain a secure, user-specific database for personal finance management. This API serves as the backend for an expense tracking application, making it easy to integrate with various frontend systems.

## Features

- **User Authentication**: Utilizes JSON Web Tokens (JWT) for secure user authentication and session management.
- **Expense Categorization**: Organize expenses into categories like Groceries, Leisure, Electronics, Utilities, and more.
- **Date-based Filtering**: Filter expenses based on timeframes like the last week, month, or a custom date range.
- **Swagger & Redoc Documentation**: Comprehensive API documentation with interactive interfaces for testing (Swagger UI and Redoc).
- **Secure Data Handling**: Each user’s expenses are securely tied to their profile, ensuring privacy and data isolation.
- **RESTful Endpoints**: Fully compliant REST API following best practices for CRUD operations.

## Technologies Used

- **Django**: The primary framework used for building the project’s backend.
- **Django REST Framework**: Provides powerful tools for creating the API, including serializers and viewsets.
- **SimpleJWT**: Manages authentication through secure token-based authentication.
- **django-filter**: Enables filtering of expenses by category and date range.
- **drf-yasg**: Used for generating Swagger UI and Redoc API documentation.
- **SQLite**: for managing persistent expense data.

## Image
![image](https://github.com/user-attachments/assets/a61966a3-0993-42ea-bb9c-620ec8c9ffd8)
