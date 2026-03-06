# Django Student 🚀 (Template, Admin Panel & Media)

This project demonstrates the **basic to intermediate workflow of Django**.
It is designed for beginners to understand how Django works internally, including
**default Admin Panel exploration and media (image upload) handling**.

## 🏗 Project Structure Overview

```
django-intro-template-admin-media/
│
├── core/
│   ├── settings.py        # Project settings (MEDIA_ROOT, MEDIA_URL)
│   ├── urls.py            # URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── navigation/            # Django app
│   ├── models.py          # Database models
│   ├── admin.py           # Admin panel customization
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── templates/             # HTML templates
│   └── include/
│
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded files (images)
│
├── manage.py
└── requirements.txt
```

## 📌 Project Overview

This project shows how:

- Django handles HTTP requests
- Views return responses
- URLs connect to views
- Templates render HTML pages
- Admin panel manages database records
- Media files are uploaded and served

## 🎯 Learning Objectives

By working with this project, you will learn:

- Django project setup
- Creating Django apps
- URL routing
- HTTP response handling
- Template rendering
- Django request → response lifecycle
- Django default admin panel exploration
- Model registration using admin decorators
- Media (image upload) configuration

## ⚡ 1. Setup Django (Run Project)

Clone Repository

bash
```
git clone https://github.com/rafi-shoishab/django-intro.git
cd django-intro
```
### Create Virtual Environment

Mac / Linux
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows
```
python -m venv .venv 
.venv\Scripts\activate
```
### Install Dependencies
```
pip install django
pip install pilow
pip install -r requirements.txt

```
### Run Development Server
```
python manage.py runserver
```
### Open browser:
```
http://127.0.0.1:8000
```
## 🌐 2. HTTP Response Implementation

### Step 2.1 — Create Django App
```
python manage.py startapp navigation
```
### Step 2.2 — Register App

📄 core/settings.py
```
INSTALLED_APPS = [
    ...
    'navigation',
]
```
### Step 2.3 — Create View

📄 navigation/views.py

```
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```

### Step 2.4 — App URLs

📄 navigation/urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

### Step 2.5 — Project URLs

📄 core/urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('navigation.urls')),
]
```

### Test:
```
http://127.0.0.1:8000/hello/
```
## 🎨 3. Template Rendering

### Step 3.1 — Create Template

📄 templates/index.html

```
<!DOCTYPE html>
<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello Django Template 🎉</h1>
</body>
</html>
```

### Step 3.2 — Configure Templates

📄 core/settings.py

```
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```

### Step 3.3 — Render Template

📄 navigation/views.py

```
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
```

🔁 Django Request → Response Flow
```
User Request
     ↓
urls.py
     ↓
views.py
     ↓
Template Rendering
     ↓
HTTP Response
```
## 🛠 4. Django Admin Panel Exploration

### Step 4.1 — Apply Migrations
```
python manage.py migrate
```
### Step 4.2 — Create Superuser
```
python manage.py createsuperuser
```
admin Login:
```
http://127.0.0.1:8000/admin/
```
### 📦 Step 4.3 — Create Model

📄 navigation/models.py

```
from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    std_id = models.IntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    dob = models.DateField()
    dept = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    image = models.ImageField(upload_to='student_img/', null=True, blank=True)

    def __str__(self):
        return self.name
```

### 🧩 Step 4.4 — Register Model Using Decorator

📄 navigation/admin.py

```
from django.contrib import admin
from .models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'std_id', 'age', 'email', 'dob', 'dept')
    search_fields = ('name', 'std_id', 'email')
    list_filter = ('dept',)
    ordering = ('id',)
```

## 🖼 5. Media (Image Upload) Configuration

### Step 5.1 — Media Settings

📄 core/settings.py

```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Step 5.2 — Serve Media Files

📄 core/urls.py

```
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Uploaded images will be stored in:

media/student_img/

## 🔧 Git Workflow (Quick Guide)

### First Time
```
git add .

git commit -m "initial commit"

git push -u origin main
```
## Daily Workflow
```
git pull

git add .

git commit -m "update message"

git push
```
### Recommended .gitignore
```
.venv/

venv/

__pycache__/

*.pyc

db.sqlite3

.DS_Store
.vscode/
media/
```
## 👨‍💻 Author

Rafiur Rahman Shoishab
GitHub: https://github.com/rafi-shoishab

## 📄 License

This project is created for educational purposes.







