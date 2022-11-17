FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000
CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py runserver 0.0.0.0:8000


