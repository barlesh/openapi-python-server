FROM python:3.8.14

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py