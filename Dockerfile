FROM python:3.12-slim

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libmariadb-dev \
        libjpeg-dev \
        libpq-dev \
        pkg-config && \
    pip3 install --no-cache -r /tmp/requirements.txt && \
    apt-get purge -y \
        build-essential \
        pkg-config && \
    apt-get autopurge -y && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /tmp/requirements.txt /var/log/apt /var/cache/apt /var/lib/apt

COPY . /app/
WORKDIR /app

RUN mkdir -p /app/static_serve/media /app/static_serve/static && \
    chown nobody:nogroup -R /app

EXPOSE 8000
USER nobody

CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn simple_personal_site.wsgi:application -b 0.0.0.0:8000
