FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./backend/manage.py .
COPY ./backend/project project
COPY ./backend/core core
EXPOSE 8000
CMD ["/bin/sh", "-c", "python manage.py collectstatic --noinput;python manage.py migrate;gunicorn --bind 0.0.0.0:8000 --workers=1 --env DJANGO_SETTINGS_MODULE=project.settings project.wsgi"]
