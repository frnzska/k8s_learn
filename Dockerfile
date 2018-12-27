FROM ubuntu:latest

RUN apt-get update -y  \
    && apt-get install -y python-pip

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app /app
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
