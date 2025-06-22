# HotelEcom

> **⚠️ NOTICE: This project is an ongoing work-in-progress and is far from complete. Many features are incomplete or subject to change. Use at your own risk!**

## Overview
HotelEcom is a Django-based e-commerce platform tailored for hotel-related products and services. The project is modular, with separate apps for accounts, products, orders, payments, notifications, and reviews.

## Features (Planned & In Progress)
- User account management and authentication
- Product listings and management
- Order processing
- Payment integration
- Notifications system
- Product reviews

## Project Structure
- `HotelEcomProj/` – Main Django project settings and configuration
- `apps/` – Contains modular Django apps:
  - `accounts/` – User accounts and permissions
  - `products/` – Product management
  - `orders/` – Order processing
  - `payments/` – Payment handling
  - `notifications/` – User/system notifications
  - `reviews/` – Product reviews
- `media/` – Uploaded files (product images, licenses, etc.)
- `requirements.txt` – Python dependencies
- `db.sqlite3` – Local development database

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd HotelEcom
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
5. **Access the app:**
   Visit `http://127.0.0.1:8000/` in your browser.

## Contributing
Contributions are welcome! Please note that the project is in early development.

