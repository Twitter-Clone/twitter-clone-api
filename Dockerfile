FROM python:latest

LABEL version="1.0"
LABEL description="Twitter Clone API"

WORKDIR /

ADD . /

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
