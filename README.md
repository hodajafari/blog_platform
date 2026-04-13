# 📝 Advanced Django Blog Platform

A fully-featured blog platform built with Django — supporting user authentication, content management, search, and dynamic post exploration.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-Backend-blue) ![SQLite](https://img.shields.io/badge/Database-SQLite-yellow) ![Live](https://img.shields.io/badge/Demo-Live-green)

---

## 📸 Screenshots

<img width="1902" height="620" alt="Unbenannt1" src="https://github.com/user-attachments/assets/e7534045-d824-4265-b294-503ac4995976" />
<img width="1852" height="828" alt="Unbenannt2" src="https://github.com/user-attachments/assets/94b0d04f-6a1c-47b8-b997-318ee1c56946" />
<img width="1906" height="550" alt="Unbenannt3" src="https://github.com/user-attachments/assets/85acc5af-bf7f-4841-b4a1-69b6c918b6ef" />




---

## ✨ Features

- **Authentication** — Login, logout, and user profile management
- **Post CRUD** — Create, edit, delete posts with image upload support
- **Comments** — Users can interact via comments on posts
- **Search** — Full-text search across posts
- **Pagination** — Clean, paginated post listing
- **Admin Panel** — Full content control via Django's built-in admin

---

## 🛠️ Tech Stack

| Layer    | Technology                      |
|----------|---------------------------------|
| Backend  | Django (Python)                 |
| Frontend | HTML, CSS, Django Templates     |
| Database | SQLite (development)            |
| Media    | Django media file handling      |

---

## ⚙️ Installation

```bash
git clone https://github.com/hodajafari/blog_platform.git
cd blog_platform
pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

Then run migrations and start the server:

```bash
python manage.py migrate
python manage.py createsuperuser   # optional: create admin account
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
blog_platform/
├── blog/
│   ├── models.py        # Post, Comment models
│   ├── views.py         # All views (list, detail, CRUD, search)
│   ├── urls.py
│   └── templates/blog/
├── users/
│   ├── models.py        # User profile
│   └── views.py         # Auth, profile views
├── media/               # Uploaded images
├── manage.py
└── requirements.txt
```

---

## 🌐 Usage

- Browse posts on the homepage
- Use the search bar to find posts by keyword
- Register or log in to create posts, comment, and manage your profile
- Admin panel available at `/admin/`

---

## 🔴 Live Demo

👉 https://blog-platform-0uly.onrender.com

---

## 👩‍💻 Author

**Hoda Jafari** — [github.com/hodajafari](https://github.com/hodajafari)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
