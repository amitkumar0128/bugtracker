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
- Integration of REST API (Read Only)

---

## Technologies Used

This project is built entirely with Django and includes:

- **Backend**: Python 3.12, Django 5.2
- **Frontend**: Bootstrap 5, HTML5, custom CSS
- **Database**: SQLite (easily swappable for PostgreSQL/MySQL)
- **Optional Enhancements**: Django REST Framework (for API extension), Static files served via Django or CDN
- **Design**: AI-generated illustrations, custom CSS styling
- **Containerization**: Docker and Docker Compose

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
    git clone https://github.com/amitkumar0128/bugtracker.git
    cd bugtracker
    ```

2. **Install Docker and docker compose**
   ```bash
   sudo apt install docker.io docker-compose-v2 -y
   ```

3.  **Start the development server:**
    ```bash
    sudo docker compose up -d
    ```

4.  **Open your browser:**
    Navigate to `http://your_public_ip/`.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

Built with ❤️ by Amitkumar.

This project was created as part of a practical learning journey into full-stack web development using Django.
