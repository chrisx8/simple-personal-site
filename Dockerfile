FROM python:3.8-slim

ARG VCS_REF
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/chrisx8/simple-personal-site"

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libmariadb-dev libjpeg-dev && \
	pip3 install --no-cache -r /tmp/requirements.txt && \
    apt-get purge -y gcc && \
    apt-get autoremove -y --purge && \
    apt-get autoclean && \
    rm -rf /tmp/requirements.txt /var/log/apt /var/cache/apt /var/lib/apt

COPY . /app/
WORKDIR /app

RUN mkdir -p /app/static_serve/media /app/static_serve/static && \
    chown nobody:nogroup -R /app && \
    cp example.env .env && \
    python3 manage.py test && \
    rm .env example.env site.db

EXPOSE 8000
USER nobody

CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn simple_personal_site.wsgi:application -b 0.0.0.0:8000
