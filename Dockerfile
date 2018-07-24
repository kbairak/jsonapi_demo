FROM python:3.6.0

RUN apt-get update
RUN apt-get install -y postgresql-client-9.4  # In order to run `./manage.py dbshell`

ENV PYTHONUNBUFFERED 1
ENV SHELLOPTS vi

ADD django_app /django_app
RUN pip install --upgrade pip
RUN pip install -r /django_app/requirements.txt

WORKDIR /django_app
CMD python kbblog/manage.py runserver 0.0.0.0:8010
