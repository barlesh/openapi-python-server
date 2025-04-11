FROM python:3.13.3

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py