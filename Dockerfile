FROM python:3.13.0a4-slim

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

RUN chmod a+rwx ./gunicorn.sh

ENTRYPOINT ["./gunicorn.sh"]

