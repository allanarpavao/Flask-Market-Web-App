# Flask Market Web App

A polished full-stack Flask marketplace application.

## 🚀 Project Overview

This project is a small e-commerce-style marketplace where users can register, log in, browse available items, purchase products with a budget, and sell items back to the market.

It demonstrates clean architecture using Flask, SQLAlchemy, Flask-Login, Flask-WTF forms, secure password hashing, and templated frontend pages.

## 🔧 Key Features

- User registration with validation and password hashing
- User login and logout flows using `Flask-Login`
- Marketplace view showing available items and owned inventory
- Secure buying and selling logic with budget tracking
- Database persistence with SQLite and SQLAlchemy ORM
- Clean separation of routes, models, forms, and extensions
- Responsive UI built with Jinja2 templates

## 🧩 Tech Stack

- Python 3
- Flask
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- SQLAlchemy
- SQLAlchemy-Utils
- python-dotenv
- SQLite

## 📁 Project Structure

- `run.py` — Flask application entrypoint
- `routes/routes.py` — page routing and market logic
- `routes/forms.py` — registration, login, purchase, and sell forms
- `models/` — ORM models for `User` and `Item`
- `extensions.py` — shared Flask extensions initialization
- `database/` — local SQLite database storage
- `templates/` — Jinja HTML templates for the app UI

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd Flask-Market-Web-App
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install Flask Flask-Login Flask-WTF Flask-Bcrypt python-dotenv SQLAlchemy SQLAlchemy-Utils
```

4. Create a `.env` file in the project root with a secure secret key:

```bash
echo "SECRET_KEY=your_super_secret_key" > .env
```

5. Start the development server:

```bash
python run.py
```

6. Open the app in your browser:

```text
http://127.0.0.1:5000
```

## ✅ Usage

- Navigate to `/register` to create a new account
- Log in at `/login`
- Visit `/market` to view items available for purchase and your inventory
- Purchase items if your budget allows
- Sell items from your owned inventory back to the market

## Project Highlights

- Secure authentication using `Flask-Login` and `Flask-Bcrypt`
- Form validation for registration and login flows
- ORM-based persistence with SQLAlchemy models

## 🚀 Future Improvements

- Add role-based access control or admin dashboard
- Introduce product categories and search/filter capabilities
- Swap SQLite for PostgreSQL or MySQL for production readiness
- Add automated tests for routes, forms, and models

## Next Steps

Ideias for improvements

1. Create an admin page for adding new gemstones or marketplace items.
   - Implement an admin-only route and template for item creation.
   - Add server-side validation for item name, price, barcode, and description.
   - Persist new items to the existing `Item` model so they appear in the marketplace immediately.

2. Add automated tests to protect usability while evolving the application.
   - Start with unit tests for `User` and `Item` business logic.
   - Add integration tests for key routes like registration, login, market purchase, and item selling.
   - Use test coverage to ensure new features do not break existing marketplace behavior.

## 📌 Notes

- The app creates the SQLite database automatically in `database/db.sqlite3`
