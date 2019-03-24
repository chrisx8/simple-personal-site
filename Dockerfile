FROM alpine:3.9

# Install system packages
RUN apk add --no-cache python3 postgresql-dev mariadb-connector-c-dev jpeg-dev zlib-dev && \
	pip3 install --no-cache --upgrade pip setuptools && \
    echo 'nameserver 127.0.0.11' > /etc/resolv.conf && \
    echo 'nameserver 1.1.1.1' >> /etc/resolv.conf && \
    echo 'nameserver 8.8.8.8' >> /etc/resolv.conf

# Install project dependencies
COPY requirements.txt /tmp/requirements.txt
RUN apk add build-base gcc python3-dev musl-dev git && \
	pip3 install --no-cache -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apk del build-base gcc python3-dev musl-dev git

# Copy code
COPY . /app/
WORKDIR /app

# Set permission and remove build tools
RUN mkdir /app/uploads && \
    chown nobody:nogroup -R /app

EXPOSE 8000
USER nobody

CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn simple_personal_site.wsgi:application -b 0.0.0.0:8000
