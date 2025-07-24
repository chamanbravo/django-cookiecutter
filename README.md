# django-cookiecutter

Cookiecutter template for django

## Usage

1. Create project from template.

   ```bash
   pip install cookiecutter
   cookiecutter gh:sandbox-pokhara/django-cookiecutter
   ```

1. Setup postgres database.

   ```bash
   psql -c "CREATE DATABASE my_project;"
   ```

1. Setup venv.

   ```bash
   cd my-project
   uv sync
   .venv\Scripts\activate.bat
   ```

1. Setup migrations and superuser.

   ```bash
   cd backend
   python manage.py makemigrations && python manage.py migrate
   python manage.py createsuperuser --user root
   ```

1. Setup sample env.

   ```bash
   task sample-env
   ```

   Note that taskfile and sample-env needs to be installed globally.

1. Run the server

   ```
   python manage.py runserver
   ```

1. Build docker image and publish to ghcr.io

   ```
   task build publish
   ```

   Note that taskfile and docker needs to be installed globally.

1. Test pre-commit. For pre-commit to run properly, git needs to be initialized first.

   ```
   git init
   git add .
   pre-commit run --all-files
   ```
