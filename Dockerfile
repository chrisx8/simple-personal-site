FROM alpine:3.8
COPY . /app/

WORKDIR /app

RUN apk add python3 py3-psycopg2 curl && \
    pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache -r requirements.txt && \
    rm /app/requirements.txt && \
    chown -R nobody:nogroup /app

EXPOSE 8000

USER nobody

CMD gunicorn wsgi:app -b 0.0.0.0:8000
