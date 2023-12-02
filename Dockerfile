FROM python:3.13.0a1

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python server.py