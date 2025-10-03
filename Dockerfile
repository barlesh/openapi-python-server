FROM python:3.14.0rc3

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py