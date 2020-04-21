# Simple Personal Site <!-- omit in toc -->

[![Build Status](https://github.com/chrisx8/simple-personal-site/workflows/build/badge.svg)](https://github.com/chrisx8/simple-personal-site/actions?query=workflow%3Abuild)
[![Docker Image Commit](https://images.microbadger.com/badges/commit/chrisx8/simple-personal-site.svg)](https://microbadger.com/images/chrisx8/simple-personal-site)

Create your personal website in minutes! Follow instructions below to set up.

## Table of Contents <!-- omit in toc -->

- [Features](#features)
- [Before installing](#before-installing)
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
- Contact form and notification email
- Link to PGP public key
- URL shortener

## Before installing

- Clone this project and enter project directory.

```bash
git clone https://github.com/chrisx8/simple-personal-site.git
cd simple-personal-site
```

- Generate a strong password [here](https://strongpasswordgenerator.com/) for database. Save it, as you'll need it during the setup process.
- Create your env file for site config.

```bash
cp example.env .env
```

- Edit `.env`, following instructions in the file.
- Generate your own icons [here](https://realfavicongenerator.net). Download the generated Favicon package.
- Unzip the downloaded package, and upload everything to `static/img/`, replacing ALL existing placeholder icon files.
- Upload an image for `og:image` (`1280*640`, in `.png` format) to `static/img/`, replacing the existing `og-image.png`

## Install with Docker

- Make sure your database is accessible from inside the container
- Set permission

```bash
sudo chown -R nobody:nogroup static
```

- Run Docker container.

```bash
# Replace [ADDRESS]:[PORT] with whereever you want the container to listen at
# When using a reverse proxy, make sure this container is NOT EXPOSED (e.g. listen on 127.0.0.1)!
docker run -d -p [ADDRESS]:[PORT] --env-file=.env -v media_files:/app/media_files/ -v $(pwd)/static:/app/static/ --restart unless-stopped --name simple-personal-site chrisx8/simple-personal-site:latest
```

- Create an admin account.

```bash
docker exec -it simple-personal-site python3 manage.py createsuperuser
```

## Install in a virtualenv

- Make sure Python 3.6 (or newer) and `pip` is installed.
- Install project dependencies.

```bash
# On Ubuntu/Debian
sudo apt-get install python3-dev libmysqlclient-dev

# On CentOS
sudo yum install rh-python36-python-devel mariadb-libs

# Create virtualenv
sudo pip3 install virtualenv
virtualenv -p $(which python3) venv

# Activate virtualenv and install dependencies
source venv/bin/activate
pip install -r requirements.txt
```

- Create system service

```bash
sudo nano /etc/systemd/system/multi-user.target.wants/personal-site.service
```

Paste in the following, and edit accordingly

```ini
[Unit]
Description=Simple Personal Site
After=network.target

[Service]
Type=simple
User=[YOUR USERNAME]
WorkingDirectory=[PROJECT DIRECTORY]
# Replace [ADDRESS]:[PORT] with whereever you want the container to listen at
# When using a reverse proxy, make sure this container is NOT EXPOSED (e.g. listen on 127.0.0.1)!
ExecStart=[PROJECT DIRECTORY]/venv/bin/gunicorn simple_personal_site.wsgi:application -b [ADDRESS]:[PORT]
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- Activate and start service

```bash
sudo systemctl daemon-reload
sudo systemctl enable personal-site
sudo systemctl start personal-site
```

- Create an admin account.

```bash
python3 manage.py createsuperuser
```

## Using HTTPS

Using HTTPS is optional but **highly recommended**. To use HTTPS:

- Set up the site behind a reverse proxy.
- For best security, make sure the reverse proxy strips incoming `X-Forwarded-Proto` header, and sets `X-Forwarded-Proto` header to `https` for HTTPS connections **only**.
- Get an SSL certificate. [Let's Encrypt](https://letsencrypt.org/) offers free certificates to everyone.
- In `.env`, set `USE_SSL=True`.

## Add content

Access the site and follow the guides on the Welcome page.

Congratulations! Now you have your personal site!

## License

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
[GNU General Public License](LICENSE) for more details.

Copyright (C) 2020 [Chris Xiao](https://github.com/chrisx8)

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

NOTE: Commits signed with GPG key ID F6C6CFB7122581AE are valid.
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEFey6cJpFXZjlcujmvbyRm4D4r30FAl5MdeQACgkQvbyRm4D4
r33noA/+MSzY5Ow76vOHp3D1G3hiv7S7iMetVytuEfOzQI/nXZ9qINBm5Njb4xiI
MrDtOpisMDOv0A8cizqUbe38ljU2aK9nGBAhB072mjWWE0d6EFMz7Tx0lK7lRzD6
1fqk4S+Nr0UYIKDdj3rSPwn9jbwg8OQXf1XhWbGyQ9kU3zoKyl8ZHCxP5F1SiuiX
53IcaE7aB/kvdPetbU59rbZBkWNjVsf73AaClNccU+malZwURyS3Xb2RFTUpFIc5
O/wkGi2d/doj/tSkBsWylh4IGnYT+a0A0WremkHmnYUCmN5mJP7DfqHGfRhRw4rG
/DV6ocr9ayF1emdQOOUwhhxuq+B1W+WR7YDDvFpbx4v6zuFQTwvgUOCeTISWO8KK
oc0aIKdpkwa181E4cu7qKNmZ83z8UFf3IiNFWPkKMq4mYdmKpn+A8e0CTZ6OSeMY
WhSM4HBiIuPa+1eyxlQv62OIWkDvGZ04aTXYuBYxwsQ3uZPZ4FvUMWCcK/In4TVQ
s6BfAcBPAh3ROQyZJbpcDSPr++96XWOoXyEhhMCNT+rp+IgpykB3hTNr+qvqjK5f
zuoKGIrOY0wHBOANCMwZJwRvrDcLSbil4MY3DJhgCpBAPGdbjSLpBnbXwCy5WGGi
FC0QrgA40tuAXMUBBusNJdUAK0T6UFXl6TIf6UUHEPXHCQFH2N8=
=Y2Lc
-----END PGP SIGNATURE-----
```
