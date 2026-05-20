FROM docker.io/library/python:3.13-slim

# Install uv
ENV UV_NO_CACHE=1
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libmariadb-dev \
        libjpeg-dev \
        libpq-dev && \
    apt-get autopurge -y && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/log/apt /var/cache/apt /var/lib/apt

# Install Python dependencies with uv
COPY pyproject.toml uv.lock /app/
WORKDIR /app
RUN uv sync --locked --no-install-project

COPY . /app/

RUN mkdir -p /app/static_serve/media /app/static_serve/static && \
    chown nobody:nogroup -R /app

EXPOSE 8000
USER nobody

CMD uv run manage.py collectstatic --noinput && \
    uv run manage.py migrate --run-syncdb && \
    uv run gunicorn simple_personal_site.wsgi:application \
        --no-control-socket \
        --bind 0.0.0.0:8000
