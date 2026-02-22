![image](https://github.com/user-attachments/assets/60c8f362-3d60-4898-8c3a-c3519656325b)
# 📰 KTN — Know The News

A Django-based web application that lets users search and browse news articles by keyword.

🌐 **Live Demo**: [https://ktn-know-the-news.onrender.com](https://ktn-know-the-news.onrender.com)

## 🚀 Features

- 🔍 Search news articles by keyword
- 📰 Clean article display
- 🎨 Simple, minimal UI

---

## 🛠️ Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.10+ |
| pip | Latest |
| Git | Any recent version |

---

## ⚙️ Installation

**1. Fork the repository**

Click the **Fork** button at the top right of this page to create your own copy.

**2. Clone your fork**

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

**3. Create a new branch**

```bash
git checkout -b feature/your-feature-name
```

**4. Navigate to the project folder**

```bash
cd news_project
```

**5. Create and activate a virtual environment**

```bash
python3 -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**6. Install dependencies**

```bash
pip install django requests
```

---

## 🔐 Environment Variables

Create a `.env` file in the root of the project:

```bash
touch .env
```

Add the following to `.env`:

```env
SECRET_KEY=your_django_secret_key_here
NEWS_API_KEY=your_news_api_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

> ⚠️ Never commit your `.env` file. Make sure it is listed in `.gitignore`.

Install `python-dotenv` to load these variables:

```bash
pip install python-dotenv
```

---

## ▶️ Running the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## ⚠️ Troubleshooting

**`ModuleNotFoundError`** — Make sure your virtual environment is active:

```bash
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

**Pylance import errors in VS Code** — Set the interpreter to `./venv/bin/python` via `Ctrl+Shift+P` → `Python: Select Interpreter`.

---

## 🤝 Contributing

1. Browse open [Issues](../../issues) and ask to be assigned before starting work
2. Fork → Clone → Branch (see Installation above)
3. Make your changes following clean coding practices
4. Push your branch and open a Pull Request

> Only work on issues you have been assigned to.

---


