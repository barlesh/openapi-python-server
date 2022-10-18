FROM python:3.10.7

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py