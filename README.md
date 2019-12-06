# Simple Personal Site <!-- omit in toc -->

[![Build Status](https://travis-ci.com/chrisx8/simple-personal-site.svg?branch=master)](https://travis-ci.com/chrisx8/simple-personal-site "Travis CI Build Status")
[![Docker Image Commit](https://images.microbadger.com/badges/commit/chrisx8/simple-personal-site.svg)](https://microbadger.com/images/chrisx8/simple-personal-site "Docker Image Commit")
[![Docker Image Size](https://images.microbadger.com/badges/image/chrisx8/simple-personal-site.svg)](https://microbadger.com/images/chrisx8/simple-personal-site "Docker Image Size")

Create your personal website in minutes! Follow instructions below to set up.

## Table of Contents <!-- omit in toc -->

- [Features](#features)
- [Before installing](#before-installing)
- [Install with Docker](#install-with-docker)
- [Install in a virtualenv](#install-in-a-virtualenv)
- [Add content](#add-content)
- [License](#license)

## Features

- Easy to manage site content
- Markdown support throughout the site
- Post blog articles
- Create project cards
- Supports video embed and images in blog articles and project cards
- Contact page with social media links and a message form

## Before installing

- Clone this project and enter project directory.

```bash
git clone https://github.com/chrisx8/simple-personal-site.git
cd simple-personal-site
```

- Generate a strong password [here](https://strongpasswordgenerator.com/) for database. Save it, as you'll need it during the setup process.
- Create your site config.

```bash
cp config.example.env config.env
```

- Edit `config.env`, following instructions in the file.
- Generate your own icons [here](https://realfavicongenerator.net). Download the generated Favicon package.
- Unzip the downloaded package, and upload everything to `static/icons/`, replacing ALL existing placeholder icon files.
- Upload an image for `og:image` (`1280*640`, in `.png` format) to `static/images/`, replacing the existing `og-image.png`

## Install with Docker

- Make sure your database is accessible from inside the container  
- Set permission

```bash
sudo chown -R 65534:65534 static
```

- Run Docker container.

```bash
# Replace "0.0.0.0:80" with wherever you want the container to listen at
docker run -d -p 0.0.0.0:80:8000 --env-file=config.env -v media_files:/app/media_files/ -v $(pwd)/static:/app/static/ --restart unless-stopped --name simple-personal-site chrisx8/simple-personal-site:latest
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
# Replace 0.0.0.0:80 with whereever you want the container to listen at
ExecStart=[PROJECT DIRECTORY]/venv/bin/gunicorn simple_personal_site.wsgi:application -b 0.0.0.0:80
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

## Add content

Access the site and follow the guides on the Welcome page.

Congratulations! Now you have your personal site!

## License

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
[GNU General Public License](LICENSE) for more details.

Copyright (C) 2019 [Chris Xiao](https://github.com/chrisx8)
