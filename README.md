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

