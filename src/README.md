# Recipe App

A modern, responsive web application for managing and sharing recipes built with Django.

## 📋 Table of Contents
- [Overview](#overview)
- [✨ Features](#features)
- [🛠️ Technologies Used](#technologies-used)
- [🚀 Live Demo](#live-demo)
- [⚙️ Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [🔄 Deployment](#deployment)
- [📱 Screenshots](#screenshots)
- [👨‍💻 About the Developer](#about-the-developer)

## Overview

The Recipe App is a full-featured Django web application designed to help users discover, manage, and share their favorite recipes. It features an intuitive interface, responsive design, and comprehensive recipe management capabilities.

## ✨ Features

- **User Authentication**: Secure login and registration system
- **Recipe Management**: Create, read, update, and delete recipes
- **Image Upload**: Add images to your recipes for visual appeal
- **Search Functionality**: Find recipes by name, ingredients, or category
- **Responsive Design**: Optimized for mobile, tablet, and desktop viewing
- **Demo Account**: Try the app with one-click login demo credentials
- **Structured Recipe Format**: Clear organization of ingredients and step-by-step instructions
- **Navigation System**: Easily browse through recipes with Next/Previous navigation

## 🛠️ Technologies Used

- **Backend**:
  - Django 5.1.1: High-level Python web framework
  - Django REST Framework 3.15.2: Toolkit for building Web APIs
  - Python 3.10+: Programming language
  - SQLite (Development) / PostgreSQL (Production): Database management
  
- **Frontend**:
  - HTML5: Semantic markup
  - CSS3: Custom styling
  - JavaScript: Interactive elements
  - Bootstrap: Responsive layout components
  
- **Deployment**:
  - PythonAnywhere: Web hosting platform
  - Git/GitHub: Version control and code management

## 🚀 Live Demo

Visit the live application: [AJ's Recipe App](https://ajsorbello.pythonanywhere.com/)

**Demo Credentials**:
- Use the "Use Demo Account" button on the login page for instant access

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/AJSorbello/recipe-app.git
    cd recipe-app
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root directory and add your environment variables:
    ```properties
    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
    ```

5. **Run the migrations**:
    ```sh
    cd src
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Collect static files**:
    ```sh
    python manage.py collectstatic
    ```

8. **Start the development server**:
    ```sh
    python manage.py runserver
    ```

9. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000`.

## 🔄 Deployment

The application is currently deployed on PythonAnywhere. To deploy your own instance:

1. **Set up a PythonAnywhere account**

2. **Create a new web app** with manual configuration (Python + Django)

3. **Clone the repository** in your PythonAnywhere console:
    ```sh
    git clone https://github.com/AJSorbello/recipe-app.git
    ```

4. **Set up a virtual environment**:
    ```sh
    cd recipe-app
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

5. **Configure your web app**:
   - Set the source code directory to `/path/to/recipe-app/src`
   - Set the working directory to `/path/to/recipe-app`
   - Configure the WSGI file to point to your Django project

6. **Create a `.env` file** with production settings:
    ```properties
    DJANGO_SECRET_KEY=your-secure-production-key
    DJANGO_DEBUG=False
    DJANGO_ALLOWED_HOSTS=yourdomain.pythonanywhere.com
    ```

7. **Run migrations and collect static files**:
    ```sh
    cd src
    python manage.py migrate
    python manage.py collectstatic
    ```

8. **Reload your web app** from the PythonAnywhere dashboard

## 📱 Screenshots

*Coming soon: Screenshots of the application showing key features and user interface.*

## 👨‍💻 About the Developer

This project was developed by AJ Sorbello, a Full-Stack Web Developer. You can find more of my projects at [ajsorbello.netlify.app](https://ajsorbello.netlify.app) or connect with me on [GitHub](https://github.com/AJSorbello) and [LinkedIn](https://www.linkedin.com/in/ajsorbello/).

---

2025 AJ Sorbello. All rights reserved.