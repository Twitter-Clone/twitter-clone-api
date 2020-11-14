FROM python:latest

LABEL version="1.0"
LABEL description="Twitter Clone API"

WORKDIR /

ADD . /

RUN pip install --upgrade pip

RUN python3 -m venv env
RUN source env/bin/activate

RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
