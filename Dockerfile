FROM python:3.11.0-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY . /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt

EXPOSE 8000
CMD python manage.py makemigrations & python manage.py migrate & python manage.py runserver 0.0.0.0:8000