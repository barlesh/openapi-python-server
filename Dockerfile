FROM python:3.14.0a2

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py