# 🐞 Bug Tracker Lite

**Bug Tracker Lite** is a lightweight, minimalist issue management system built using Django. It allows developers and teams to track, manage, and resolve software bugs efficiently. This project focuses on functionality, clarity, and simplicity—making it ideal for internal teams or solo developers who need a fast, no-frills way to manage bug reports.

---

## Overview

The system includes core bug tracking features: user authentication, bug creation, assignment, status management, and a visual dashboard to get an at-a-glance view of all bugs in the system. The frontend uses Bootstrap for a clean and responsive UI, with custom styling to enhance readability and professional appearance. Designed as a fully local project, it can also be easily deployed to the cloud with a few changes.

---

## Features

- Full authentication system (Register, Login, Logout)
- Create, update, and delete bug reports
- Assign bugs to specific users
- Track bug status (Open, In Progress, Resolved)
- Dashboard with dynamic bug summaries
- Human-readable timestamps
- Minimalist, modern UI with mobile responsiveness
- Clean admin panel for project management
- DRY code structure using Django's class-based views
- Easy to extend into a team collaboration or project management tool

---

## Technologies Used

This project is built entirely with Django and includes:

- **Backend**: Python 3.12, Django 5.2
- **Frontend**: Bootstrap 5, HTML5, custom CSS
- **Database**: SQLite (easily swappable for PostgreSQL/MySQL)
- **Optional Enhancements**: Django REST Framework (for API extension), Static files served via Django or CDN
- **Design**: AI-generated illustrations, custom CSS styling

---

## Screenshots

### Homepage  
![Homepage](screenshots/Home.png)

### Login Page  
![Login](screenshots/Login.png)

### Dashboard  
![Dashboard](screenshots/Dashboard.png)

### Bug Details  
![Bug Details](screenshots/Bug-List.png)

_All screenshots are located in the `/screenshots` directory._

---

## How to Run the Project Locally

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/amitkumar0128/bugtracker.git](https://github.com/amitkumar0128/bugtracker.git)
    cd bugtracker
    ```

2.  **Create and activate a virtual environment:**

    * **Linux/macOS:**
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an administrative user.

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Open your browser:**
    Navigate to `http://127.0.0.1:8000/`.

## Deployment Notes

To prepare for production deployment:

* Set `DEBUG = False` in your project's `settings.py` file.
* Add your domain name or server IP address to the `ALLOWED_HOSTS` setting in `settings.py`.
* Run `python manage.py collectstatic` to gather all static files into a single directory.
* Consider using production-ready WSGI servers like Gunicorn or uWSGI along with a reverse proxy like NGINX.
* You can also deploy this project on platforms like Heroku, Railway, or Render, which provide specific deployment workflows for Python/Django applications.

## Project Structure

bugtrack/
├── bugtracker/         # Main Django project directory
│   ├── bugs/           # Django application containing models, views, forms, etc.
│   │   ├── models.py   # Defines the data models for bugs and related entities
│   │   ├── views.py    # Handles the application's logic and renders templates
│   │   ├── forms.py    # Defines forms for user input
│   │   ├── urls.py     # Defines the URL patterns for the 'bugs' application
│   │   └── ...
│   ├── bugtracker/     # Django project settings and configurations
│   │   ├── settings.py # Contains important project settings (database, DEBUG mode, etc.)
│   │   ├── urls.py     # Defines the project-level URL patterns
│   │   └── ...
│   ├── db.sqlite3       # Local development database (not for production)
│   ├── manage.py        # Django's command-line utility
│   ├── static/          # Directory for static files (CSS, JavaScript, images)
│   │   └── ...
│   └── templates/       # Directory for HTML templates
│       ├── base.html     # Base template for other HTML files
│       ├── bugs/         # Templates specific to the 'bugs' application
│       │   ├── bug_list.html
│       │   ├── bug_form.html
│       │   └── ...
│       ├── dashboard.html  # Template for the user dashboard
│       └── registration/ # Templates for user registration and login
│           ├── login.html
│           └── register.html
├── requirements.txt  # Lists the Python dependencies for the project
└── README.md         # The main README file with project instructions

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

Built with ❤️ by Amitkumar.

This project was created as part of a practical learning journey into full-stack web development using Django.