FROM python:3.12.0a3

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py