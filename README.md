# 📝 Advanced Django Blog Platform

A fully-featured blog platform built with Django, supporting user interaction, content management, and dynamic content exploration.

---

## 🚀 Features

### 👤 User System

* 🔐 User authentication (Login / Logout)
* 🧑‍💼 User profiles
* 📝 User-specific content management

### ✍️ Blog Management

* Create, update, and delete posts (CRUD)
* Upload images for posts
* Rich post detail pages

### 💬 Interaction

* Comment system on posts
* User engagement with content

### 🔎 Content Discovery

* Search functionality for posts
* Pagination for better navigation
* Organized post listing

### 🛠️ Admin & Backend

* Django admin panel for full content control
* ORM-based database management

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Django Templates
* **Database:** SQLite (development)
* **Media Handling:** Django media system

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/hodajafari/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open:
http://127.0.0.1:8000/

---

## 👩‍💻 Example Code

### Sample Django View

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

---

## 🌐 Usage

* Visit homepage to browse posts
* Use search to find specific content
* Navigate pages using pagination

After login:

* Create posts
* Comment on posts
* Manage your profile

---

## 🔴 Live Demo

👉 https://blog-platform-0uly.onrender.com

---

## 👨‍💻 Author

**Hoda Jafari**
GitHub: https://github.com/hodajafari
