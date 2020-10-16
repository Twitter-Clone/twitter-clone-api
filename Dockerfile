FROM python:latest

LABEL version="1.0"
LABEL description="Twitter Clone API"

WORKDIR /

ADD . /

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver"]
