# Banking Management System

This repository contains a banking management system.

## How to Run the Code

To run this code on your local machine, follow these steps:

1. Install Django on your PC by entering the following command in the command prompt (CMD):
   ```
   pip install django
   ```

2. Download or clone this repository to your local machine.

3. Open a command prompt (CMD) and navigate to the project folder.

4. In the command prompt, run the following command to start the Django server:
   ```
   python manage.py runserver
   ```

5. Once the server is running, open a web browser and enter the following URL:
   ```
   http://127.0.0.1:8000/
   ```

6. You should now be able to access the banking management system and use its features.

Please note that you may need to modify the database settings in the project's configuration files to match your local environment.

## Project Structure

The repository includes the following files and directories:

- `README.md`: This file provides an overview of the project and instructions for running the code.
- `manage.py`: The Django project's management script.
- `BMSapp/`: The main Django project directory.
  - `settings.py`: The project's settings file, including database configuration and other Django-specific settings.
  - `urls.py`: The project's URL configuration.
  - `wsgi.py`: The entry point for the project's WSGI application.
- `BANKapp/`: The Django app directory containing the banking management system's implementation.
  - `models.py`: Defines the models for the banking system, including customer accounts and transactions.
  - `views.py`: Contains the views (or controllers) that handle user requests and render responses.
  - `urls.py`: The URL configuration specific to the banking app.
  - `templates/`: Contains HTML templates for rendering the web pages.
  - `static/`: Contains static files such as CSS and JavaScript.

Feel free to explore and modify the code according to your needs.

## Contributors

- Suman Monadal
- Sahil Nandy
- Sneha Paul
- Suthirtha Paramanik
- Susneha Chowdhury
- Payal Karmakar

If you have any questions or suggestions, please feel free to contact any of the contributors listed above.
