FROM python:3.7-alpine
WORKDIR /app
RUN apk add python3-dev argon2 libffi-dev build-base jpeg-dev zlib-dev git gcc \
 libc-dev postgresql-dev linux-headers mariadb-connector-c-dev;\
  pip install uwsgi
COPY requirements.txt /app/
RUN pip install -r requirements.txt ;\
  pip install -e git+git://github.com/theatlantic/django-mysqlndb-backend.git@v1.1.0#egg=django-mysqlndb-backend
COPY . /app