# 📚 Library Management System
This is a Django-based Library Management System with MySQL as the database. It allows administrators to perform CRUD operations on books and provides a student view for checking available books.

# 🚀 Features
Admin Panel: Manage books (Add, Update, Delete, View).

Student View: View available books in the library.

REST API: Built using Django REST Framework for book management.

MySQL Database: Stores book records securely.

# 🛠️ Tech Stack
Backend: Django, Django REST Framework

Database: MySQL

Frontend: (To be decided—Django templates, React, or another framework)

# 📥 Installation
1️⃣ Clone the Repository
```
git clone https://github.com/your-username/library-management.git
cd library-management
```
2️⃣ Set Up a Virtual Environment
```
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate  # Windows
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Configure Database
Create a MySQL database and update settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
5️⃣ Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
6️⃣ Create a Superuser
```
python manage.py createsuperuser
```
7️⃣ Start the Server
```
python manage.py runserver
```

# 🔗 Future Enhancements
✅ Search & Filter Books

✅ User Authentication (Students & Admins)

✅ Borrow & Return Book System

✅ Frontend using React or Django Templates


