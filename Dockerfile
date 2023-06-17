FROM python:3.12.0b1

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py