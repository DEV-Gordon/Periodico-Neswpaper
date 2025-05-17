# Newspaper Website

A modern newspaper website built with Django and Tailwind CSS. Features include:
- Category-based article organization
- Featured articles
- Admin panel for content management
- Responsive design
- Image handling for articles

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Features

### Admin Panel
- Manage categories
- Create and edit articles
- Set featured articles
- Upload images

### Frontend
- Responsive design with Tailwind CSS
- Category navigation
- Featured articles section
- Article detail pages with related articles
- Pagination for article listings

## Project Structure

- `news/` - Main application directory
  - `models.py` - Database models for Category and Article
  - `views.py` - View logic for displaying content
  - `admin.py` - Admin panel configuration
  - `urls.py` - URL routing

- `templates/` - HTML templates
  - `base.html` - Base template with navigation
  - `news/` - News app templates
    - `home.html` - Homepage template
    - `category.html` - Category page template
    - `article_detail.html` - Article detail template

- `static/` - Static files (CSS, JS, images)
- `media/` - Uploaded media files

## Database Configuration

This project uses **MySQL** as the database engine. Make sure you have a MySQL server running and a database named `newspaper` already created.

To connect the Django project to your database, update the `settings.py` file with the following configuration:

```python
DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'newspaper',      # Name of the database (schema)
     'USER': 'root',           # MySQL username
     'PASSWORD': 'zasca',      # MySQL password
     'HOST': '127.0.0.1',      # Server address (can also be 'localhost')
     'PORT': '3306',           # Default MySQL port
 }
}