Project Overview
Your task is to develop a Django project in a domain of your choice, ideally one you're familiar with or passionate about. This project should demonstrate your proficiency with Django, RESTful API design, and integration with third-party services.

Core Requirements:
Domain-Specific Django Project
Choose a domain you're interested in or currently working in.
The project must have at least 10 Django models.
Database Connectivity
Use Postgres if your birthday is in summer or winter, or MySQL otherwise.
User Authentication
Implement user roles with different permissions (admins and non-admins).
Implement Google OAuth for user authentication.
RESTful API
Develop a REST API with both public and private endpoints.
Implement various types of authentication, including a custom auth method.
Include features like filtration, pagination , and Swagger documentation.
Implement endpoints for user login, registration, and logout.
GraphQL Integration
Incorporate a read-only GraphQL interface.
Celery for Asynchronous Tasks
Set up a Celery server for background tasks.
Create tasks for Telegram integration (e.g., sending messages as a bot) and reporting to Google Sheets.
Use Redis as a broker if your birth date is odd, or RabbitMQ otherwise.
Dockerization
Dockerize the entire project, including services and database migrations.
Use Gunicorn as the WSGI server in Docker for Django in production.
Testing and Quality Assurance
Write comprehensive unit tests for the project.
Set up a GitHub Action for continuous integration, which checks code style, runs tests, and measures test coverage.
