FROM python:3.14.2

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py