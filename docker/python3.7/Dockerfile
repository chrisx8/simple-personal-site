FROM python:3.7-alpine

ARG VCS_REF
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/chrisx8/simple-personal-site"

RUN apk add --no-cache postgresql-dev mariadb-connector-c-dev jpeg-dev zlib-dev && \
    echo 'nameserver 127.0.0.11' > /etc/resolv.conf && \
    echo 'nameserver 1.1.1.1' >> /etc/resolv.conf && \
    echo 'nameserver 8.8.8.8' >> /etc/resolv.conf

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache build-base gcc musl-dev git && \
	pip3 install --no-cache -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apk del build-base gcc musl-dev git

COPY . /app/
WORKDIR /app

RUN mkdir /app/uploads && \
    chown nobody:nogroup -R /app

EXPOSE 8000
USER nobody

CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn simple_personal_site.wsgi:application -b 0.0.0.0:8000
