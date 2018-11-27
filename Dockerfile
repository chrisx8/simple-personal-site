FROM alpine:3.8
COPY . /app/

WORKDIR /app

RUN apk add --no-cache python3 py3-psycopg2 curl && \
    pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install --no-cache -r requirements.txt && \
    echo 'nameserver 127.0.0.11' > /etc/resolv.conf && \
    echo 'nameserver 1.1.1.1' >> /etc/resolv.conf && \
    echo 'nameserver 8.8.8.8' >> /etc/resolv.conf && \
    rm /app/requirements.txt && \
    chown -R nobody:nogroup /app && \
    python3 manage.py collectstatic && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate --run-syncdb

EXPOSE 8000

USER nobody

CMD gunicorn simple_personal_site.wsgi:application -b 0.0.0.0:8000
