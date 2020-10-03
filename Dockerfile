FROM python:latest

LABEL version="1.0"
LABEL description="Twitter Clone API"

WORKDIR /

ADD . /

RUN python3 -m venv twitter-clone-env
#RUN source twitter-clone-env/bin/activate

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

#CMD ["python3", "manage.py", "migrate", "&&", "python3", "manage.py", "createsuperuser", "&&", "python3", "manage.py", "runserver"]
CMD ["python3", "manage.py", "runserver"]
#RUN python3 manage.py migrate \
# && python3 manage.py createsuperuser \
# && python3 manage.py runserver
