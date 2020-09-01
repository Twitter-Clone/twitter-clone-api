FROM python:latest

WORKDIR /

ADD . /

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m venv env
RUN virtualenv twitter_clone

# CMD []
