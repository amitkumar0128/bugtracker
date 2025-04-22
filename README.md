# 🐞 Bug Tracker Lite

A lightweight Django-based bug tracking system to create, assign, and resolve issues.

## 🚀 Features
- User Authentication (Login/Register/Logout)
- Role-based assignments (Reporter/Developer)
- CRUD operations on bugs
- Filters by severity/status
- Clean Bootstrap UI

## 🛠 Tech Stack
- Django 5.2
- SQLite
- Bootstrap 5
- Deployed on Render (or Railway)

## 📸 Screenshots
<!-- Upload and embed screenshots here -->
![Screenshot 2025-04-22 215153](https://github.com/user-attachments/assets/dc75bfa8-6806-4f4c-84e3-890f5b103b99)
![Screenshot 2025-04-22 215212](https://github.com/user-attachments/assets/3584b75b-b0cc-4359-b9cd-abfc1a6a3531)
![Screenshot 2025-04-22 215359](https://github.com/user-attachments/assets/9777d13e-9b7a-45ca-af02-8523d4a21d75)
![Screenshot_22-4-2025_215724_127 0 0 1](https://github.com/user-attachments/assets/f958519d-1cbb-4c19-8f46-eefb40c384d7)
![Screenshot 2025-04-22 215804](https://github.com/user-attachments/assets/da304dd0-a718-43d3-818e-7ff21cb2db55)

## 💻 Run Locally

```bash
git clone https://github.com/amitkumar0128/bugtracker.git
cd bugtracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
