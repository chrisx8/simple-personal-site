# Simple Personal Site <!-- omit in toc -->

[![build](https://github.com/chrisx8/simple-personal-site/actions/workflows/build.yml/badge.svg)](https://github.com/chrisx8/simple-personal-site/actions/workflows/build.yml)

A fast and minimalist Django-based CMS for developers and tech enthusiasts.

## Table of Contents <!-- omit in toc -->

- [Features](#features)
- [Before installing](#before-installing)
- [Installation](#installation)
  - [Install with Docker](#install-with-docker)
  - [Install in a virtualenv](#install-in-a-virtualenv)
- [Using HTTPS](#using-https)
- [Add content](#add-content)
- [License](#license)

## Features

- Easy-to-manage site content
- Markdown support throughout the site
- Post blog articles
- Create project cards
- Embed code blocks in blog posts
- Video and image embed in blog articles and project cards
- Show social media links in footer
- Contact form
- Host PGP public key
- URL shortener

## Before installing

- Clone this project and enter project directory.

```bash
git clone https://github.com/chrisx8/simple-personal-site.git
cd simple-personal-site
```

- Generate a strong password for the database. Save it, as you'll need it during
  the setup process.
- Create your env file for site config.

```bash
cp .env.example .env
```

- Edit `.env`, following instructions in the file.
- Generate your own icons: <https://realfavicongenerator.net>. Download the
  generated Favicon package.
- Unzip the downloaded package and upload everything to `static/img/`, replacing
  all existing placeholder icon files.
- Upload a banner image for `og:image` (`1280*640`, in `.png` format) to
  `static/img/`, replacing the existing `og-image.png`

## Installation

### Install with Docker

- Make sure your database is accessible from inside the container
- Create directory for static files

```bash
mkdir -p static_serve/media staic_serve/static
sudo chown -R nobody:nogroup static_serve
```

- Run Docker container.

```bash
# Replace [ADDRESS]:[PORT] with wherever you want the container to listen at
# When using a reverse proxy, make sure this container is NOT EXPOSED to the
# Internet! (e.g. listen on 127.0.0.1)
docker run -d -p [ADDRESS]:[PORT] \
  --env-file=.env \
  -v $(pwd)/static_serve:/app/static_serve \
  -v $(pwd)/static:/app/static/ \
  --restart unless-stopped \
  --name simple-personal-site \
  ghcr.io/chrisx8/simple-personal-site:latest
```

- Create an admin account.

```bash
docker exec -it simple-personal-site python3 manage.py createsuperuser
```

- Set up a web server (such as Apache or Nginx) to serve static files.
  - Serve `static_serve/media` at `/media/`
  - Serve `static_serve/static` at `/static/`
  - DO NOT serve `static/`
  - [Sample Nginx config](sps-nginx.example.conf)

### Install in a virtualenv

- This site supports Python 3.10-3.14.
- Make sure Python and `uv` are installed.
- Install project dependencies.

```bash
# Bootstrap virtualenv and install dependencies with uv
uv sync

# Activate virtualenv
source .venv/bin/activate
```

- Start server

```bash
# Replace [ADDRESS]:[PORT] with wherever you want the container to listen at
# When using a reverse proxy, make sure this container is NOT EXPOSED to the
# Internet! (e.g. listen on 127.0.0.1)
gunicorn simple_personal_site.wsgi:application -b [ADDRESS]:[PORT]
```

- Create an admin account.

```bash
python3 manage.py createsuperuser
```

- Set up a web server (such as Apache or Nginx) to serve static files
  - Serve `static_serve/media` at `/media/`
  - Serve `static_serve/static` at `/static/`
  - DO NOT serve `static/`
  - [Sample Nginx config](sps-nginx.example.conf)

## Using HTTPS

Using HTTPS is optional but **highly recommended**. To use HTTPS:

- Set up the site behind a reverse proxy.
  [Sample Nginx config](sps-nginx.example.conf)
- For best security, make sure the reverse proxy strips incoming
  `X-Forwarded-Proto` header, and sets `X-Forwarded-Proto` header to `https` for
  HTTPS connections **only**.
- Get an SSL certificate. [Let's Encrypt](https://letsencrypt.org/) offers free
  certificates to everyone.
- In `.env`, set `USE_SSL=True`.

## Add content

Access the site and follow the guides on the Welcome page.

Congratulations! Now you have your personal site!

## License

[MIT License](LICENSE)

Copyright (C) 2018-2023 [Chris Xiao](https://github.com/chrisx8)
