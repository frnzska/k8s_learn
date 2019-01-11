FROM python:3 as build-env

COPY . /app
RUN cd /app && python script.py


FROM alpine
WORKDIR /app
COPY --from=build-env /app/ /app/script
ENTRYPOINT /app/script
