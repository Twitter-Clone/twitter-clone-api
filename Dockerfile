FROM python:latest

LABEL version="1.0"
LABEL description="Twitter Clone API"

WORKDIR /

ADD . /

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m venv env
RUN virtualenv twitter_clone

CMD ["python3", "manage.py", "migrate", "\", 
 "&&", "python3", "manage.py", "createsuperuser", "\",
 "&&", "python3", "manage.py", "runserver", "0.0.0.0:8000"]

