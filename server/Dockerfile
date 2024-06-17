FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y gettext
COPY . /app/

ENV VIRTUAL_ENV /.env

EXPOSE 3003


CMD ["gunicorn", "--bind", ":3003", "--workers", "3", "abocados.wsgi:application"]
