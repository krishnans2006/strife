# Strife

A Discord clone, written in Django.


## Features

- Create Servers, channels, and roles
- Control user permissions
- Send/receive messages in real-time (no refreshing required!)
- Upload attachments, send emoji, etc.
- Customize your user profile


### In Progress

- Reactions
- Message edits/deletions

### Future Plans

- Message replies
- Markdown support
- Custom emoji
- Online/status indicators
- Direct messages


## Setup

### 1. Clone the repository

```bash
git clone git@github.com:krishnans2006/strife.git
cd strife
```

### 2. Install dependencies

```bash
poetry install
```

### 3. Set up the database

```bash
poetry run python manage.py migrate
```

### 4. Set up live reload for development

```bash
poetry run python manage.py tailwind install
```

### 5. Run the server

```bash
poetry run python manage.py runserver
poetry run python manage.py tailwind start
```

(In two separate terminals at once).


## File Structure

- `strife/`
  - `apps/` - Django functionality
    - `channels/`
    - `emoji/`
    - `home/`
    - `messages/`
    - `reactions/`
    - `roles/`
    - `servers/`
    - `users/`
  - `settings/` - Django project settings
  - `static/` - Static files
    - `default-avatars/`
    - `js/`
  - `templates/` - Generic HTML templates
  - `theme/` - Tailwind configuration


### App Structure

- `messages/`
  - `migrations/` - Database migrations (version control for database schema)
  - `templates/messages/` - App-specific HTML templates
  - `__init__.py`
  - `admin.py` - Django admin configuration
  - `apps.py` - Defines app properties (like the Django app_label)
  - `consumers.py` - Non-HTTP request handling (Django Channels)
  - `models.py` - Database models
  - `routing.py` - Non-HTTP routing (Django Channels)
  - `urls.py` - HTTP URL routing
  - `views.py` - HTTP request handling
