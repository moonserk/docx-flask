FROM python:3

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

RUN chmod a+rwx ./gunicorn.sh

ENTRYPOINT ["./gunicorn.sh"]
