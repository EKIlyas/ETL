FROM python:3.9-alpine as base

FROM base as builder

RUN mkdir /install
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /install
COPY postgres_to_es/requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
RUN apk --no-cache add libpq
COPY Deploy/postgres_to_es/entrypoint.sh /pg2es/entrypoint.sh
RUN chmod 777 /pg2es/entrypoint.sh
COPY postgres_to_es/*.py /pg2es/
WORKDIR /pg2es

ENTRYPOINT ["/pg2es/entrypoint.sh"]
