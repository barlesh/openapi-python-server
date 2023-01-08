FROM python:3.11.1

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py